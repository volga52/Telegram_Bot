# import ipaddress
# import pathlib
import os

# from pydantic import BaseSettings, SecretStr

from setting.setting_core import Settings

# class Settings(BaseSettings):
#     # Желательно вместо str использовать SecretStr
#     # для конфиденциальных данных, например, токена бота
#     bot_container_name: str = 'bot_container_name'
#     bot_image_name: str = 'botimage_name'
#     bot_name: str
#     bot_token: SecretStr
#     admins: list
#     use_redis: bool
#
#     db_user: str = 'volga52'
#     pg_password: SecretStr = 'examplePostgresPass'
#     db_pass: SecretStr = 'pg_password'
#     db_name: str
#     db_host: ipaddress.IPv4Address
#
#     # Вложенный класс с дополнительными указаниями для настроек
#     class Config:
#         # Имя файла, откуда будут прочитаны данные
#         # (относительно текущей рабочей директории)
#         # env_file = '.env'
#         env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"
#         # Кодировка читаемого файла
#         env_file_encoding = 'utf-8'


config = Settings()

BOT_ID = 1573514660

BOT_CONTAINER_NAME = config.bot_container_name
BOT_IMAGE_NAME = config.bot_image_name
BOT_NAME = config.bot_name
BOT_TOKEN = config.bot_token.get_secret_value()
ADMINS = config.admins
USE_REDIS = config.use_redis

DB_USER = config.db_user
PG_PASSWORD = config.pg_password.get_secret_value()
DB_PASS = config.db_pass.get_secret_value()
DB_NAME = config.db_name
DB_HOST = config.db_host

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, DB_NAME)


if __name__ == '__main__':
    # При импорте файла сразу создастся
    # и провалидируется объект конфига,
    # который можно далее импортировать из разных мест

    for key, value in config:
        print(f'{key}: {value} <{type(value)}>')
