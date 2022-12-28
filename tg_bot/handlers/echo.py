from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher


async def bot_echo(message: types.Message):
    await message.answer(f'Эхо без состояния\nСообщение\n{message.text}')


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    await message.answer(f'Эхо состояние {state_name}\nСообщение'
                         f'\n{message.text}')


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(
        bot_echo_all, state='*', content_types=types.ContentType.ANY)
