import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TELEGRAM CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", "0"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Harry009876")

LOGGER_ID = int(getenv("LOGGER_ID", "0"))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DATABASE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = getenv("MONGO_DB_URI")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MUSIC SETTINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GITHUB CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nobitasir251/ALPHA_MUSIC"
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HEROKU CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SUPPORT CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/TanyaUpdatesBot"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/TanyaSupportChat"
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BUTTON CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BUTTON_COLOUR = getenv("BUTTON_COLOUR", "True").lower() == "true"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SPOTIFY CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# STRING SESSIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BOT SETTINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = (
    getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
)

BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

DEBUG_IGNORE_LOG = True


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IMAGE CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/fu6jk3.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/26nzoq.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"

TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# URL VALIDATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL and not re.match(
    r"^https?://", SUPPORT_CHANNEL
):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match(
    r"^https?://", SUPPORT_CHAT
):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHAT must start with https://"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# REQUIRED VARIABLES VALIDATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise SystemExit(
        "[ERROR] - API_ID, API_HASH and BOT_TOKEN are required."
    )

if not OWNER_ID:
    raise SystemExit("[ERROR] - OWNER_ID is required.")

if not LOGGER_ID:
    raise SystemExit("[ERROR] - LOGGER_ID is required.")

if not MONGO_DB_URI:
    raise SystemExit("[ERROR] - MONGO_DB_URI is required.")
