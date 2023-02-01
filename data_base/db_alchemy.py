from os import path

from sqlalchemy import create_engine, inspection
from sqlalchemy.orm import sessionmaker

from setting.config import DATABASE
from data_base.dbcore import Base

# from settings import config, utility
# from models.category import Category
# from models.product import Products
# from models.order import Order
# from models.errand import Errand
# from settings import utility

from sqlalchemy import Column, DateTime, Integer, Boolean


class Singleton(type):
    """
    Паттерн Singleton предоставляет механизм создания одного
    и только одного объекта класса,
    и предоставление к нему глобальную точку доступа.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """
    Класс менеджер для работы с БД
    """

    def __init__(self):
        """
        Инициализация сессии и подключение к БД
        """
        self.engine = create_engine(DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(DATABASE):
            Base.metadata.create_all(self.engine)

    def close(self):
        """Закрывает сессию"""
        self._session.close()
