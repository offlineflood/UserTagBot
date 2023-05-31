import os

class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    #>>> https://t.me/BotFather
    API_ID = int(os.environ.get("API_ID","8173444"))
    API_HASH = os.environ.get("API_HASH","8ce53801c1b49cd4d2fa108eb151b255")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6152708456:AAF2xfhqFeUEVzB01pHVWKbzyTmewczaUys")
    BOT_NAME = os.environ.get("BOT_NAME", "₪ ๏ᴜʀ 𝙏𝙖𝙜 𝘽𝙤𝙩 ˢⁱⁿ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "OUR_TaggerBot")
    BOT_ID = int(os.environ.get("BOT_ID","6152708456"))
    Dejavu = os.environ.get("Dejavu","1280040987").split()
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "MUCVE_M")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1280040987"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","OUR_SupportGroup")
    SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL","OUR_SupportKanal")