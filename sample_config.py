from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

HEROKU = (
    bool(environ.get("DYNO"))  # NOTE Make it false if you're not deploying on heroku or docker.
)

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", "5014285587:AAHv95jed8jrvwDgLOEvQUSfAdgod7EKjCE")
    API_ID = int(environ.get("API_ID", 18622297))
    API_HASH = environ.get("API_HASH", "27e6993af0786f66f96599db6cd10bcc")
    SESSION_STRING = environ.get("SESSION_STRING", "AQCKwdEiBvj9ALOnkwLT4kBQlJPR06ZOQe4kW8IAtGksAx6fU65MLjuuAyoul6D7mquzgGDLSCMe7Ur8j73ljYMGPIrcbJlKZjdrP6x3NIo8iIWfZUF4FRDMmUkTGmSb06uZ4nyWBSVMiFxQEU8DtPjIkKXAkIITehtl8rhhCir3cJ-lxNorkhEWdN4jTa-f6zXbKkY17I8SXsUoAUxOinGKFcPUyUfgAkOMR6ui37puOgDqFgOLFwD3IgWrJipfJzRpEdv83T_IyT9fVb97VxmfMX3NZm8bFw983HpnWEFtYltL2fPmR9kE0_H854lDBEJR5gSybfPatQs32AqduihJev6VsAA")
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", -1001726870449))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", -1001726870449))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", -1001726870449))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", 30))
    MONGO_URL = environ.get("MONGO_URL", "mongodb://mongo:LOEgdfz9JY11BRbH9E89@containers-us-west-24.railway.app:5949")
    ARQ_API_URL = environ.get("ARQ_API_URL", "https://thearq.tech/")
    ARQ_API_KEY = environ.get("ARQ_API_KEY", "SPGHHO-JIWZUR-KEQPQU-ZJFQFT-ARQ")
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", -1001726870449)))
    RSS_DELAY = int(environ.get("RSS_DELAY", 300))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", True)))
else:
    BOT_TOKEN = "467677575:YZfaakjwd545dfg-N6JStihhuw5gQeZHntc"
    API_ID = 123456
    API_HASH = "dfxcgs5s12hdcxfgdfz"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+916969696969"  # Need for Userbot
    SUDO_USERS_ID = [
        4543744343,
        543214651351,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -100125431255
    GBAN_LOG_GROUP_ID = -100125431255
    MESSAGE_DUMP_CHAT = -1001181696437
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://username:password@cluster0.ksiis.mongodb.net/YourDataBaseName?retryWrites=true&w=majority"
    ARQ_API_KEY = "Get this from @ARQRobot"
    ARQ_API_URL = "https://thearq.tech"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
