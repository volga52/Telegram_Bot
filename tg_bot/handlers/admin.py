from aiogram import types
from aiogram.dispatcher import Dispatcher


async def admin_start(message: types.Message):
    await message.reply('Hello, admin!')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['start'])
