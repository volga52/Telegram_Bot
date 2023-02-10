from handlers.handlers_com import HandlersCommands, HandlerEcho
from handlers.handler_fsm import HandlersFSM


class HandlerMain:
    """Класс компоновщик"""
    def __init__(self, dp):
        self.dp = dp
        # Инициализация обработчиков
        self.handler_commands = HandlersCommands(self.dp)
        self.handler_fsm = HandlersFSM(self.dp)
        # Самый последний класс обработчик
        self.handler_echo = HandlerEcho(self.dp)

    def handle(self):
        # Запускаем обработчики
        self.handler_commands.handler()
        self.handler_fsm.handler()

        self.handler_echo.handler()
