from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


bot = Bot(token='')
dp = Dispatcher(bot)


# @dp.message_handler()
# async def get_message(message: types.Message):
#     chat_id = message.chat.id
#     # text = message.text
#     text = 'Некоторый текст'
#
#     # await bot.send_message(chat_id=chat_id, text=text)
#     send_message = await bot.send_message(chat_id=chat_id, text=text)
#     print(send_message.to_python())


@dp.message_handler()
async def get_message(message: types.Message):
    send_message = await bot.send_photo(chat_id=None, photo='')
    print(send_message.photo[-1].file_unique_id)
    # У каждого фото свой id

    result = await bot.set_chat_title(chat_id=None, title='Новое название')
    print(result)

    invite_link = await bot.export_chat_invite_link(chat_id=None)
    print(invite_link)

    bot_user = await bot.get_me()
    print(bot_user.username)


executor.start_polling()
