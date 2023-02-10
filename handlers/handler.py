import abc
# import markup.markup as kb
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, dp: Dispatcher = None):
        self.dp = dp
        self.bot = dp.bot
        self.markup = Keyboards()
        # self.storage = MemoryStorage()

    @abc.abstractmethod
    async def handler(self):
        pass
