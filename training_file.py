from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from setting.config import config, DATABASE


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    # text = message.text
    text = 'Некоторый текст'

    # await bot.send_message(chat_id=chat_id, text=text)
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())


executor.start_polling(dp)
