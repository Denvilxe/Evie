import logging
import os
import sys
import time
import os
import urllib.parse as urlparse
import bmemcached
import json
from logging import basicConfig
from logging import DEBUG
from logging import getLogger
from logging import INFO

from telethon import TelegramClient
from telethon.sessions import StringSession
import spamwatch
StartTime = time.time()
CMD_LIST = {}
CMD_HELP = {}
CMD_FUN = {}
FUN_LIST = {}
LOAD_PLUG = {}
LUNA_VERSION = "1.8.1"
Telethon_Version = "1.20.0"
# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
ENV = bool(os.environ.get("ENV", True))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    GBAN_LOGS = os.environ.get("GBAN_LOGS", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    WHITE_LIST = {int(x) for x in os.environ.get("WHITE_LIST", "").split()}
    API_KEY = os.environ.get("API_KEY", None)
    API_HASH = os.environ.get("API_HASH", None)
    KEY_2 = os.environ.get("KEY_2", None)
    HASH_2 = os.environ.get("HASH_2", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    DB_URI = os.environ.get("DATABASE_URL")
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    WOLFRAM_ID = os.environ.get("WOLFRAM_ID", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    tbot = TelegramClient(None, API_KEY, API_HASH)
    SUDO_USERS = list(SUDO_USERS)
    DEV_USERS = list(DEV_USERS)
    WHITE_LIST = list(WHITE_LIST)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    WALL_API = os.environ.get("WALL_API", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    TEMP_MAIL_KEY = os.environ.get("TEMP_MAIL_KEY", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    STRING_2 = os.environ.get("STRING_2", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    TEMPORARY_DATA = os.environ.get("TEMPORARY_DATA", None)
    UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL", None)
    CONSOLE_LOGGER_VERBOSE = os.environ.get("CONSOLE_LOGGER_VERBOSE", "False")
    BOT_ID = int(os.environ.get("BOT_ID", None))
    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=DEBUG
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)
    if not SPAMWATCH_API:
        sw = None
    else:
       try:
          sw = spamwatch.Client(SPAMWATCH_API)
       except:
          sw = None
    if STRING_SESSION:
        ubot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
    else:
        sys.exit(1)
    if STRING_2:
         abot = TelegramClient(StringSession(STRING_2), KEY_2, HASH_2)
         try:
            abot.start()
         except BaseException:
            pass
    try:
        ubot.start()
    except BaseException:
        print("Error Dude !")
        sys.exit(1)
    mc = bmemcached.Client(os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','), os.environ.get('MEMCACHEDCLOUD_USERNAME'), os.environ.get('MEMCACHEDCLOUD_PASSWORD'))
else:
    sys.exit(1)
