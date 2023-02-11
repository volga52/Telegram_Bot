from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMFirst(StatesGroup):
    category = State()  # Вид животного
    name = State()
    photo = State()
    breed = State()     # Порода
    description = State()
