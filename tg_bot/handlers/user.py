from aiogram import Dispatcher
from aiogram.types import Message

from tg_bot.services.setting_commands import set_starting_commands


async def user_start(message: Message):
    await message.reply('Hello, user!')
    await set_starting_commands(message.bot, message.from_user.id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'], state='*')
