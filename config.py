from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 6))
    API_HASH = getenv("API_HASH", None)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", 6228366286))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "RADHE_KRISHNA_HARE_HARE")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "NOBITA_X_SUPPORT")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1001819078701"))
    MONGO_URI = getenv("MONGO_DB_URI", None)
    DB_NAME = getenv("DB_NAME", "NOBITA_X_ROBOT")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
