from dataclasses import dataclass

from environs import Env


@dataclass
class Bots:
    bot_token: str


@dataclass
class DataBase:
    db_password: str


@dataclass
class Settings:
    bots: Bots
    password: DataBase


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(bot_token=env.str("TOKEN")),
        password=DataBase(db_password=env.str("PASSWORD")),
    )


settings = get_settings("input")
