from pyrogram import Client, filters, idle
from pyrogram.types import Message
from Config import Config

app = Client(
    "Dejavu Tag Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)


#---------------------------------------------------------------GROUP GIREKEN SALAMLAMA MSJ------------------------------------------------------------------------------#
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qruplardakı userləri tag etmək üçün yaradıldım.\n🤖Kömək üçün /start yazmaq kifayətdir.✨**''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#
        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply(f'🤖 [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME})-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

app.start()
print(f"Bot başladı... Botu işə salın!")
idle()
