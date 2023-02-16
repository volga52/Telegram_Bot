from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton

from handlers.handler import Handler


class HandlerInline(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн-кнопки
    """

    def __init__(self, dp: Dispatcher):
        super().__init__(dp)

    def menu_out(self):
        self.markup.new_markup()

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        ...
        Функция присутствует для понимания процесса работы кнопок
        Используемая в коде функция находится в файле markup.py
        """
        # return InlineKeyboardButton(str(name), callback_data=str(name.id))
        return InlineKeyboardButton(str(name), callback_data=str(name))

    async def handle_inline_buttons(self, data):
        await self.dp.bot.answer_callback_query(data.id,
                                                'Нажата inline кнопка')
        await self.dp.bot.send_message(data.from_user.id,
                                       f'Нажата inline кнопка {data.data}')

    def handler(self):
        dp = self.dp

        @dp.callback_query_handler(lambda call: True)
        # @dp.callback_query_handler(lambda call: call.data == 'users_url')
        async def process_first_inline_button(call: types.CallbackQuery):
            await self.handle_inline_buttons(call)
