from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, \
    BotCommandScopeChat

STARTING_COMMANDS = {
    'ru': [
        BotCommand('start', 'Начать заново'),
        BotCommand('get_commands', 'Получить список команд'),
        BotCommand('reset_command', 'Сбросить команды'),
    ],
    'eng': [
        BotCommand('start', 'Start over'),
        BotCommand('get_commands', 'Get a list of commands'),
        BotCommand('reset_command', 'Reset Commands'),
    ]
}


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(commands=[
        BotCommand('command_default_1', 'Стандартная команда 1'),
        BotCommand('command_default_2', 'Стандартная команда 2'),
        BotCommand('command_default_3', 'Стандартная команда 3'),
        ], scope=BotCommandScopeDefault()
    )


async def set_starting_commands(bot: Bot, chat_id: int):
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )
