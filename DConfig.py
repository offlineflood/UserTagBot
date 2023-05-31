import os

class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    #>>> https://t.me/BotFather
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_NAME = os.environ.get("BOT_NAME")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_ID = int(os.environ.get("BOT_ID"))
    Dejavu = os.environ.get("Dejavu","1280040987").split()
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1280040987"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP")
    SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL")
