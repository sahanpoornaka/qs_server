from pydantic import BaseSettings, BaseModel
from functools import lru_cache
import configparser

deta_config = configparser.ConfigParser()
deta_config.read('app/conf/deta.ini')


class Settings(BaseSettings):
    app_name: str = "QS"
    server_env: str = "LOCAL"
    serve_ip: str = "0.0.0.0"
    serve_port: int = 8000

    # class Config:
    #     env_file = ".env"


class DetaSettings(BaseModel):
    deta_username: str = "neura"
    deta_password: str = "zaq123WSX"
    deta_project_key: str = "c06xk2uq_YSXPpiHNhKPBNHBG9EDdkCHWGDfDrGhL"


class AppSettings(BaseModel):
    env_settings: Settings
    deta_settings: DetaSettings


@lru_cache()
def get_settings():
    settings = AppSettings(
        env_settings=Settings(),
        deta_settings=DetaSettings.parse_obj(deta_config[Settings().server_env]),
    )
    # settings = AppSettings(**docdb_config[Settings().server_env])
    return settings
