from typing import Callable

from dotenv import dotenv_values, set_key

class Settings:
    ENV: str = "development"
    DB: str ='case_challenge'
    DB_USER: str ='case_challenge'
    DB_PASSWORD: str ='TEST'
    DB_PORT: str ='5433'
    DB_HOST: str ='localhost'
    
    WEB_SERVER_HOST: str = "localhost"
    WEB_SERVER_PORT: int = 8000
    WEB_SERVER_RELOAD: bool = True

    def __init__(self, **entries):
        self.__dict__.update(entries)


def _configure_initial_settings() -> Callable[[], Settings]:
    env_values = dict(dotenv_values())

    env_values['WEB_SERVER_PORT'] = int(env_values['WEB_SERVER_PORT'])

    settings = Settings(**env_values)


    def fn() -> Settings:
        return settings

    return fn


get_settings = _configure_initial_settings()
