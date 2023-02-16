from handlers.handlers_com import HandlersCommands, HandlerEcho
from handlers.handler_fsm import HandlersFSM
from handlers.handler_inline import HandlerInline
from handlers.handler_inline_bot import HandlerInlineMode


class HandlerMain:
    """Класс компоновщик"""
    def __init__(self, dp):
        self.dp = dp
        # Инициализация обработчиков
        self.handler_commands = HandlersCommands(self.dp)
        self.handler_fsm = HandlersFSM(self.dp)
        self.handler_inline = HandlerInline(self.dp)
        self.handler_inline_mode = HandlerInlineMode(self.dp)
        # Самый последний класс обработчик
        self.handler_echo = HandlerEcho(self.dp)

    def handle(self):
        # Запускаем обработчики
        self.handler_commands.handler()
        self.handler_fsm.handler()
        self.handler_inline.handler()
        self.handler_inline_mode.handler()

        self.handler_echo.handler()
