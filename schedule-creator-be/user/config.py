from typing import Any
from pydantic import BaseSettings
from decouple import config
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    """Server config settings"""

    # name of app
    app_name: str = "User Service"

    root_url = config("ROOT_URL", default="http://0.0.0.0:8000")

    # current running environment
    env = config("ENV", default="dev")

    # aws credentials
    aws_secret = config("AWS_SECRET_ACCESS_KEY")
    aws_access = config("AWS_ACCESS_KEY")

    dev_url = config("DEV_URL")

    # Mongo Engine settings
    mongo_uri = config("MONGO_URI")

    # Security settings
    authjwt_secret_key = config("SECRET_KEY")
    #authjwt_denylist_enabled: bool = True
    #authjwt_denylist_token_checks: set = {"access", "refresh"}
    access_expires = timedelta(minutes=15)
    refresh_expires = timedelta(days=30)
    salt = config("SALT").encode()

    class Config:
        env_file = "user/.env"
        orm_mode = True


'''
async def initiate_database():
    try:
        client = AsyncIOMotorClient(CONFIG.mongo_uri)
        await init_beanie(database=client['test'],
                          document_models=[User, Workspace, Result, Contact, Provider, Log, Verification])

    except Exception as e:
        print(e)
'''
CONFIG = Settings()




