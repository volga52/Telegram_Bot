import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, pre, code, italic
from aiogram.types import ParseMode, InputMediaVideo, InputMediaPhoto, \
    ChatActions, ContentType
from emoji import emojize

from setting.config import BOT_TOKEN
from markup import markup as kb


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
               '/test', '/testpre', '/info', '/play', '/hikb1',
               '/hikb2', '/hikb3', '/hikb4', '/hikb5', '/hikb6',
               '/hikb7', '/rmkbs', '/firstbtn', '/secondbtn', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN_V2)


# Демонстрация работы клавиатур
@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button_first_dtn(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Нажата первая кнопка!')


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id,
                                        text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\n'
                 'А этот текст может быть длиной до 200 символов 😉',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           f'Нажата инлайн кнопка! code={code}')


@dp.message_handler(commands=['play'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)


@dp.message_handler(commands=['hikb1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры",
                        reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['hikb2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия",
                        reply_markup=kb.greet_kb2)


@dp.message_handler(commands=['hikb3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок",
                        reply_markup=kb.markup3)


@dp.message_handler(commands=['hikb4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд",
                        reply_markup=kb.markup4)


@dp.message_handler(commands=['hikb5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок",
                        reply_markup=kb.markup5)


@dp.message_handler(commands=['hikb6'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\n"
                        "Эти две кнопки не зависят друг от друга\n"
                        "В Telegram Desktop пока нельзя делиться геолокацией",
                        reply_markup=kb.markup_request)


@dp.message_handler(commands=['hikb7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Седьмое - все методы вместе",
                        reply_markup=kb.markup_big)


@dp.message_handler(commands=['rmkbs'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений",
                        reply_markup=kb.ReplyKeyboardRemove())


@dp.message_handler(commands=['firstbtn'])
async def process_command_first_btn(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['secondbtn'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_kb_full)
# Конец демонстрации работы клавиатур


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


@dp.message_handler(commands=['note'])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # Конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)


@dp.message_handler(commands=['file'])
async def process_file_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)
    await bot.send_document(user_id, TEXT_FILE,
                            caption='Это супер-пупер файл')


@dp.message_handler(commands=['testpre'])
async def process_testpre_command(message: types.Message):
    # message_text = emojize(':smirk: Does not work')
    # message_text = emojize('\N{Smirking Face}')
    # message_text = emojize('\U0001F600 All right')

    # message_text = emojize(':open_file_folder: Ds fhgj')
    message_text = pre(emojize("""@dp.message_handler(commands=['testpre'])
async def process_testpre_command(message: types.Message):
    message_text = pre(emojize('Ха! Не в этот раз \N{Smirking Face}'))
    await bot.send_message(message.from_user.id, message_text)"""))
    await bot.send_message(message.from_user.id, message_text,
                           parse_mode=ParseMode.MARKDOWN_V2)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN_V2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
