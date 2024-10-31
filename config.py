import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "23861777"))
API_HASH = os.environ.get("API_HASH", "16104c9a6a05c337237819a218d46c5d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8095772116:AAFYdvAkmnMEXfEw_hVPOh6TjYxddZs3UmY")
ADMIN = int(os.environ.get("ADMIN", "6672752177"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "omniscient_reader_view_poinnt")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "logsnarutorename"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://patelbhart45y666:yUY67YQZis7FS1op@cluster0.zsmsb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "renamebot")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/a095dc9dc288a142615b8-8d3f123470412ab17c.jpg")
