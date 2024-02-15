from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    mongodb_uri:str = os.getenv('MONGODB_URI')
    secret_key:str = os.getenv('SECRET_KEY')
    algorithm:str = os.getenv('ALGORITHM')

    model_config = SettingsConfigDict(env_file=".env")