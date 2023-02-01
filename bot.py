from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode, InputMediaVideo, InputMediaPhoto
from emoji import emojize

from setting.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


CAT_BIG_EYES = 'AgACAgIAAxkDAAMvY9ljutWlHQpQSY0G1zKUyUfMExIAAg_HMRtdPMlKoV2pgOTsuh0BAAMCAAN4AAMtBA'
KITTENS = [
    'AgACAgIAAxkDAAMzY9lju8hedMaDRyvmwkzKNSyLwFAAAhDHMRtdPMlKIBv1pfTPdqUBAAMCAAN3AAMtBA',
    'AgACAgIAAxkDAAM0Y9ljuzaR4190U8flhsVouHYbGRsAAhHHMRtdPMlK-OnsufPfooQBAAMCAAN4AAMtBA',
    'AgACAgIAAxkDAAM1Y9ljvMrDL_Zq-Kxmg-qdOlM7qMQAAhLHMRtdPMlKgii2JWFXPwoBAAMCAANtAAMtBA',]
VOICE = 'AwACAgIAAxkDAAMwY9ljulPmgkLh7HQQGJBmC49bQZQAAr8kAAJdPMlK4lDf-4C6UUktBA'
VIDEO = 'BAACAgIAAxkDAAMyY9ljulT3ymV89O7cTy14luH9lbYAAsEkAAJdPMlKZdpKQ5ddTzwtBA'
TEXT_FILE = 'BQACAgIAAxkDAAMuY9ljt5VDyPvAcvSDyQABuWRSdH13AAK-JAACXTzJStnUdlxn4dR1LQQ'
VIDEO_NOTE = 'DQACAgIAAxkDAAMxY9ljupaVFHGTCFx4hXIf0Jid6IYAAsAkAAJdPMlKK2I6jZr-jYgtBA'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!\nИспользуй /help,"
                        "чтобы узнать список доступных команд!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    # await message.reply("Напиши мне что-нибудь, и я отправлю этот текст "
    #                     "тебе в ответ!")
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file',
               '/test', '/info', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['test'])
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")


@dp.message_handler(commands=['info'])
async def print_info(message: types.Message):
    # chat_id = message.chat.id
    text = 'Инфа отправлена'
    print(message.to_python())

    # send_message = await bot.send_message(chat_id=chat_id, text=text)
    send_message = await message.answer(text, parse_mode='HTML')
    print(send_message.to_python())


@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_voice(message.from_user.id, VOICE,
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Какие глазки! :eyes:'
    await bot.send_photo(message.from_user.id, CAT_BIG_EYES,
                         caption=emojize(caption),
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    media = [InputMediaVideo(VIDEO, 'Ёжик и котята')]
    for photo_id in KITTENS:
        media.append(InputMediaPhoto(photo_id))
    await bot.send_media_group(message.from_user.id, media)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
