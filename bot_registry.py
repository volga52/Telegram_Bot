from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from setting.config import BOT_TOKEN

from handlers.handler_main import HandlerMain


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

handlers = HandlerMain(dp)
handlers.handle()

# executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
