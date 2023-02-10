from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

from FSM.first_fsm import FSMFirst
from handlers.handler import Handler


class HandlersFSM(Handler):
    """Класс обрабатывает машинное состояние """

    def __init__(self, dispacher):
        self.storage = MemoryStorage()
        super().__init__(dp=dispacher)
        self.dp.storage = self.storage


    async def dialog_animal_start(self, message: types.Message):
        await FSMFirst.category.set()
        await message.reply('Какое у тебя животное?')

    async def animal_category(self, message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['category'] = message.text
        await FSMFirst.next()
        await message.reply('Теперь введи имя')

    async def animal_name(self, message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMFirst.next()
        await message.reply('Загрузи фото')

    async def animal_photo(self, message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMFirst.next()
        # await message.reply(f"Порода животного {state.proxy()['category']}")
        await message.reply(f"Порода твоего животного")

    async def animal_breed(self, message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['breed'] = message.text
        await FSMFirst.next()
        await message.reply('Еще немного описания')

    async def animal_description(self, message: types.Message,
                                 state: FSMContext):
        async with state.proxy() as data:
            data['description'] = message.text
            print('OK')
        async with state.proxy() as data:
            await message.reply(str(data))

        await state.finish()

    def handler(self):
        self.dp.register_message_handler(self.dialog_animal_start,
                                         commands=['animal'], state=None)
        self.dp.register_message_handler(self.animal_category,
                                         state=FSMFirst.category)
        self.dp.register_message_handler(self.animal_name,
                                         state=FSMFirst.name)
        self.dp.register_message_handler(
            self.animal_photo, content_types=['photo'], state=FSMFirst.photo)
        self.dp.register_message_handler(self.animal_breed,
                                         state=FSMFirst.breed)
        self.dp.register_message_handler(self.animal_description,
                                         state=FSMFirst.description)
