from handlers.handler import Handler
# from markup.markup import Keyboards


class HandlerInline(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн-кнопки
    """
    def menu_out(self):
        self.markup.new_markup()

    def all(self):
        pass
