import asyncio

from emoji import emojize
from aiogram import types
from aiogram.utils.markdown import text, bold, pre, code, italic
from aiogram.types import ParseMode, InputMediaVideo, InputMediaPhoto, \
    ChatActions, ContentType, ReplyKeyboardRemove

from handlers.handler import Handler
from setting.messages import *


class HandlersCommands(Handler):
    """
    Класс обрабатывает основные входящие команды (/start, /help)
    """
    def __init__(self, dispatcher):
        super().__init__(dispatcher)

    async def process_start_command(self, message: types.Message):
        await message.reply("Привет!\nНапиши мне что-нибудь!\nИспользуй /help,"
                            "чтобы узнать список доступных команд!",
                            reply_markup=self.markup.menu_on_start())

    async def process_help_command(self, message: types.Message):
        msg = text(bold(HELP_PREVIEW), *HELP_COMMAND_LIST, sep='\n')
        await message.reply(msg, parse_mode=ParseMode.MARKDOWN_V2)

    async def any_message(self, message: types.Message):
        await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
        await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")

    async def print_info(self, message: types.Message):
        text = 'Инфа отправлена'
        print(message.to_python())

        send_message = await message.answer(text, parse_mode='HTML',
                                            reply_markup=ReplyKeyboardRemove())
        print(send_message.to_python())

    async def process_description_command(self, message: types.Message):
        await message.answer(DESCRIPTION, parse_mode="HTML")

    async def process_voice_command(self, message: types.Message):
        await self.bot.send_voice(message.from_user.id, VOICE,
                                  reply_to_message_id=message.message_id)

    async def process_photo_command(self, message: types.Message):
        caption = 'Какие глазки! :eyes:'
        await self.bot.send_photo(message.from_user.id, CAT_BIG_EYES,
                                  caption=emojize(caption),
                                  reply_to_message_id=message.message_id)

    async def process_group_command(self, message: types.Message):
        media = [InputMediaVideo(VIDEO, 'Ёжик и котята')]
        for photo_id in KITTENS:
            media.append(InputMediaPhoto(photo_id))
        await self.bot.send_media_group(message.from_user.id, media)

    async def process_note_command(self, message: types.Message):
        user_id = message.from_user.id
        await self.bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
        await asyncio.sleep(
            1)  # Конвертируем видео и отправляем его пользователю
        await self.bot.send_video_note(message.from_user.id, VIDEO_NOTE)

    async def process_file_command(self, message: types.Message):
        user_id = message.from_user.id
        await self.bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
        await asyncio.sleep(1)
        await self.bot.send_document(user_id, TEXT_FILE,
                                     caption='Это супер-пупер файл')

    async def process_testpre_command(self, message: types.Message):
        message_text = pre(emojize(TESTPRE))
        await self.bot.send_message(message.from_user.id, message_text,
                                    parse_mode=ParseMode.MARKDOWN_V2)

    async def echo_message(self, msg: types.Message):
        await self.bot.send_message(msg.from_user.id, msg.text)

    def handler(self):
        self.dp.register_message_handler(self.process_start_command,
                                         commands=['start'])
        self.dp.register_message_handler(self.process_help_command,
                                         commands=['help'])
        self.dp.register_message_handler(self.any_message, commands=['test'])
        self.dp.register_message_handler(self.print_info, commands=['info'])
        self.dp.register_message_handler(self.process_voice_command,
                                         commands=['voice'])
        self.dp.register_message_handler(self.process_photo_command,
                                         commands=['photo'])
        self.dp.register_message_handler(self.process_group_command,
                                         commands=['group'])
        self.dp.register_message_handler(self.process_note_command,
                                         commands=['note'])
        self.dp.register_message_handler(self.process_file_command,
                                         commands=['file'])
        self.dp.register_message_handler(self.process_testpre_command,
                                         commands=['testpre'])
        self.dp.register_message_handler(self.process_description_command,
                                         commands=['description', 'Описание'])
        # Самая последняя регистрация
        self.dp.register_message_handler(self.echo_message)

    # @dp.message_handler(content_types=ContentType.ANY)
    # async def unknown_message(msg: types.Message):
    #     message_text = text(emojize(UNKNOWN), italic('\nЯ просто напомню,'),
    #                         'что есть', code('команда'), '/help')
    #     await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN_V2)
