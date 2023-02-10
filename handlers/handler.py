import abc
# import markup.markup as kb
from aiogram.dispatcher import Dispatcher


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, dp: Dispatcher = None, markup=None):
        self.dp = dp
        self.bot = dp.bot
        self.markup = markup

    @abc.abstractmethod
    async def handler(self):
        pass
