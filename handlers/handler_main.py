from handlers.handlers_com import HandlersCommands


class HandlerMain:
    """Класс компоновщик"""
    def __init__(self, dp):
        self.dp = dp
        # Инициализация обработчиков
        self.handler_commands = HandlersCommands(self.dp)

    def handle(self):
        # Запускаем обработчики
        self.handler_commands.handler()
