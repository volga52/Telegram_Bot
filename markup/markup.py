from aiogram import types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')
button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')

markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)
markup4 = ReplyKeyboardMarkup().row(button1, button2, button3)
markup5 = ReplyKeyboardMarkup().row(button1, button2, button3
                                    ).add(KeyboardButton('Средний ряд'))

markup5.row(button4, button5)
markup5.insert(button6)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(
    'Отправить свой контакт ☎️', request_contact=True)).add(KeyboardButton(
    'Отправить свою локацию 🗺️', request_location=True))

# ******************************************************************

markup_big = ReplyKeyboardMarkup()

markup_big.add(button1, button2, button3, button4, button5, button6)
markup_big.row(button1, button2, button3, button4, button5, button6)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))

# *******************************************************************

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''",
                                           switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'",
                                           switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате",
                                           switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton(
    'Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))


class Keyboards:
    """
    Класс Keyboards предназначен для создания разметки интерфейса бота
    """
    def __init__(self):
        self.markup = None
        self.BD = None

    def menu_on_start(self):
        button01 = KeyboardButton('/test')
        button02 = KeyboardButton('/info')
        button03 = KeyboardButton('/Описание')
        button04 = KeyboardButton('/animal')

        self.markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                          one_time_keyboard=True)
        self.markup.add(button01).add(button02).insert(button03)
        self.markup.row(button01, button04, button03)

        return self.markup

    @staticmethod
    def set_inline_btn(text, call_name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        """
        # return InlineKeyboardButton(str(name), callback_data=str(name.id))
        return InlineKeyboardButton(str(text), callback_data=str(call_name))

    async def url_command(self, message: types.Message):
        url_kb = InlineKeyboardMarkup(row_width=1)  # ширина ряда

        url_button1 = InlineKeyboardButton(text='Ссылка1',
                                           url='http://youtube.com')
        url_button2 = InlineKeyboardButton(text='Ссылка2', url='http://ya.ru')
        url_kb.add(url_button1, url_button2)

        # await message.answer('Ссылочки', reply_markup=url_kb)
        return url_kb

    def first_inline_kb(self):
        kb_first = InlineKeyboardMarkup()

        but_1 = self.set_inline_btn('PRESSED', 'users_url')
        # but_1 = InlineKeyboardButton(text='PRESSED', callback_data='users_url')

        kb_first.add(but_1)

        return kb_first
