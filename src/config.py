from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# class Settings(BaseSettings):
#     db_host: str
#     db_port: int
#     db_name: str
#     db_user: str
#     db_pass: str
#
#     class Config:
#         env_file = "../.env"
#
# settings = Settings()

# @lru_cache()
# def get_settings():
#     return Settings()
