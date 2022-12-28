from dataclasses import dataclass
from environs import Env


@dataclass
class Tgbot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    # def __int__(self):
    tg_bot: Tgbot = None
    db: DbConfig = None
    misc: Miscellaneous = None


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=Tgbot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS")
        ),
        db=DbConfig(
            host=env.str("DB_HOST"),
            password=env.str("DB_PASS"),
            user=env.str("DB_USER"),
            database=env.str("DB_NAME")
        ),
        misc=Miscellaneous()
    )
