from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

HEROKU = (
    bool(environ.get("DYNO"))  # NOTE Make it false if you're not deploying on heroku or docker.
)

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_URL = environ.get("MONGO_URL", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
else:
    BOT_TOKEN = "5014285587:AAHv95jed8jrvwDgLOEvQUSfAdgod7EKjCE"
    API_ID = 18622297
    API_HASH = "27e6993af0786f66f96599db6cd10bcc"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+13085714955"  # Need for Userbot
    SUDO_USERS_ID = [
        1511373882,
        163494588,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = 724778836
    GBAN_LOG_GROUP_ID = -1001726870449
    MESSAGE_DUMP_CHAT = -1001726870449
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb://mongo:LOEgdfz9JY11BRbH9E89@containers-us-west-24.railway.app:5949"
    ARQ_API_KEY = "SPGHHO-JIWZUR-KEQPQU-ZJFQFT-ARQ"
    ARQ_API_URL = "https://thearq.tech"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
