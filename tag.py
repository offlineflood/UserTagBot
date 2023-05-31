from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
import random, asyncio, logging
from telethon import Button
from Config import Config 

logging.basicConfig(level=logging.INFO,format='%(name)s - [%(levelname)s] - %(message)s')
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
dejavu = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
tekli_calisan = []
  
@dejavu.on(events.NewMessage(pattern="^/help$"))
async def start(event):
     await event.reply(f"**[{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME})-un kömək “📚 Əmrlər„ bunlardır.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**㋡⇰ /tag “səbəb„ - 5-li Tag Atışları.**\n**㋡⇰ /etag “səbəb„ - Emoji ilə etiketlər.**\n**㋡⇰ /stag “səbəb„ - Söz'lü Tag etiketlər.**\n**㋡⇰ /tektag “səbəb„ - Üzvləri Tək-Tək etiketlər.**\n**㋡⇰ /usta “səbəb„ - usta Tag Bot'una aid Tag etiketlər.**\n**㋡⇰ /admins “səbəb„ - İdarəçilər Tək-Tək etiketlər.**\n**㋡⇰ /cancel - Tag Ələməyi Dayandır.**\n•━━━━━━━━•••━━━━━━━━•",
                       buttons=(
	            [Button.url("💡Bot Keç", f"https://t.me/{Config.BOT_USERNAME}?start=start")],
	            [Button.url('💬 Qrup', f'https://t.me/{Config.SUPPORT_GROUP}'),
		           Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],
              ),
              link_preview=False)
       
@dejavu.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in dejavu.iter_participants(event.chat_id):
     user = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"◆━━━━━━━▣✦▣━━━━━━━━◆\n🤖 Salam {user} xoş gördük.\n\nMənim adım [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) mən faydalı xüsusiyyətləri olan teleqram etiket botuyam.\nQruplarda üzvləri etiket etmək səlahiyyətinə sahibəm.\n\n🤖 Ətraflı məlumat üçün “📚 Əmrlər„ bölməsinə daxil olun.\n◆━━━━━━━▣✦▣━━━━━━━━◆",
                       buttons=(
	            [Button.inline(f"📚 Əmrlər", data="help"),
	             Button.inline(f"📑 Təkliflər", data="reklam")],
              [Button.url('✜ Qrupa əlavə et ✜',f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")],
	            [Button.url('💬 Qrup', f"https://t.me/{Config.SUPPORT_CHANNEL}"),
               Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],
              ),
              link_preview=False)
     
  if event.is_group:
    return await dejavu.send_message(event.chat_id, f"** [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME})'un əmrlər üçün?\nBot'a daxil olub.**",
                                     buttons=(
              [Button.url("💡Bot Keç", f"https://t.me/{Config.BOT_USERNAME}?start=start")],
	            [Button.url('💬 Qrup', f'https://t.me/{Config.SUPPORT_GROUP}'),
		           Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],
              ),
              link_preview=False)

@dejavu.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in dejavu.iter_participants(event.chat_id):
     user = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"◆━━━━━━━▣✦▣━━━━━━━━◆\n🤖 Salam {user} xoş gördük.\n\nMənim adım [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) mən faydalı xüsusiyyətləri olan teleqram etiket botuyam.\nQruplarda üzvləri etiket etmək səlahiyyətinə sahibəm.\n\n🤖 Ətraflı məlumat üçün “📚 Əmrlər„ bölməsinə daxil olun.\n◆━━━━━━━▣✦▣━━━━━━━━◆",
                      buttons=(
	            [Button.inline(f'📚 Əmrlər', data="help"),
	             Button.inline(f'📑 Təkliflər', data="reklam")],
              [Button.url('✜ Qrupa əlavə et ✜',f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")],
	            [Button.url('💬 Qrup', f'https://t.me/{Config.SUPPORT_GROUP}'),
               Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],
              ),
              link_preview=False)

@dejavu.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"**[{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME})-un kömək “📚 Əmrlər„ bunlardır.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**㋡⇰ /tag “səbəb„ - 5-li Tag Atışları.**\n**㋡⇰ /etag “səbəb„ - Emoji ilə etiketlər.**\n**㋡⇰ /stag “səbəb„ - Söz'lü Tag etiketlər.**\n**㋡⇰ /tektag “səbəb„ - Üzvləri Tək-Tək etiketlər.**\n**㋡⇰ /usta “səbəb„ - usta Tag Bot'una aid Tag etiketlər.**\n**㋡⇰ /admins “səbəb„ - İdarəçilər Tək-Tək etiketlər.**\n**㋡⇰ /cancel - Tag Ələməyi Dayandır.**\n•━━━━━━━━•••━━━━━━━━•",
                     buttons=(
	            [Button.inline(f"◅ Geri", data="start"),
               Button.url('📺 Kanal', f"https://t.me/{Config.SUPPORT_CHANNEL}")],
              ),
              link_preview=False)

@dejavu.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**[{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) Təkliflər üçün sahib'lə əlaqə saxlaya bilərsiniz.**",
                     buttons=(
		          [Button.url('🎉 Sahib', f'https://t.me/{Config.OWNER_USERNAME}')],
	            [Button.url('💬 Qrup', f'https://t.me/{Config.SUPPORT_GROUP}'),
                Button.url('📺 Kanal', f"https://t.me/{Config.SUPPORT_CHANNEL}")],
	            [Button.inline(f"◅ Geri", data="start")]
              ),
              link_preview=False)
    
@dejavu.on(events.NewMessage(pattern='^/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  
@dejavu.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır!**")
  
  admins = []
  async for admin in dejavu.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag əməliyyatı uğurla dayandırıldı!**")
        return
      if usrnum == 5:
        await dejavu.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await dejavu.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@dejavu.on(events.NewMessage(pattern='^/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@dejavu.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")
  
  admins = []
  async for admin in dejavu.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:   
        await dejavu.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag əməliyyatı uğurla dayandırıldı! **")
        return
      if usrnum == 5:   
        await dejavu.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@dejavu.on(events.NewMessage(pattern='^/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@dejavu.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! **")
  
  admins = []
  async for admin in dejavu.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**↯ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await dejavu.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1:
        await dejavu.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@dejavu.on(events.NewMessage(pattern='^/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	
stag = (
"Bəzi insanlar yağışı hiss edər, digərləri isə sadəcə islanar",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz",
"Heç bir ruhun ağrısı sənin dərdindən az deyil",
"Mən hər şeyi sınayıram; amma bacardığımı edirəm.",
"Sevgi bir qadının həyatının bütün hekayəsidir və bir kişinin yeganə macərasıdır.",
"Xoşbəxtlik ilk növbədə bədən sağlamlığındadır.",
"Nə qədər yaşadığımız deyil, necə yaşadığımızdır",
"Yer göy qurşağı, ağıl prizma, varlıq isə ağ şüadır.",
"Hara getdiyinizi bilmirsinizsə, hansı tərəfə getdiyinizin əhəmiyyəti yoxdur.",
"Həyatın ən qiymətli vaxtıdır. Kimə hədiyyə etdiyinizə diqqət edin.",
"Evin bütün pəncərələrini sındırıb, sonra qapını döyə bilməzsən.",
"Xoşbəxtlik yaşadığın həyat tərzində deyil, həyata baxış tərzindədir.",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz.",
"Bu həyatda yarım nəfəs. Sevgidən başqa heç nə planlaşdırma...",
"Hər kəsə içindəki yaxşılar qədər yaxşı bir həyat arzulayıram.",
"Gözəlliyi gözəl edən ədəbdir, ədəb isə gözəlliyi sevmək üçün səbəbdir!",
"Qızılgülün ətri qızılgül verənin əlində qalır",
"Axtardığın şey səni axtarandır.",
"Hətta bir quş da göydə qanad çırpar.",
"Könül almağı bilməyənlərə həyat əmanət deyil.",
"Dürüst olmaqdan qorxma, ən çox itirəcəyiniz yanlış insanlar olacaq.",
"İnsan ağac deyil, qırılanda səs çıxararsan.",
"Öyrənmək həyatın yeganə sübutudur.",
"Dünya əhalisi artdıqca insanların sayı azalır.",
"Layiq olmadığını düşündüyünüz insanlara əsla həqiqəti deməyin.",
"Çox şükür ki, göy hələ heç bir pul kisəsinə sığmır.",
"Özün ol. Artıq hamı götürüb.",
"Zərər çəkdim, boğazımdakı düyünləri uddum.",
"O qədər gözəl gülümsəyirdi ki, sevməsəydim boşuna olardı.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Zamanla hər şeyə alışırsan, amma bitmir.",
"Əgər həqiqəti deyirsənsə, heç nəyi xatırlamağa ehtiyac yoxdur.",
"Həqiqəti ilk söyləyən siz olun... Əks halda kimsə sizin yerinizə mütləq həqiqəti söyləyəcək.",
"Kişilər daha güclü ola bilər, amma qadınlar dözümlüdürlər.",
"Ağrı üçün heç bir resept yoxdur",
"Ardınca getməyə cəsarətiniz varsa, bütün arzular gerçəkləşə bilər.",
"Bu gizli sevgidir, heç kimə dərdlərimi deyə bilmərəm.",
"Sizcə sevgi hər şeyi bağışlayır?",
"Mənə də, sənə də siqaret lazımdır",
"Mən səndən xüsusi birini tanımırdım",
"Bir gün sevgi bitər, xatirələr qalır",
"Sevmək nə qədər uzun bir sözdür!",
"Hatırladığım en unutulası şeysin.",
"Birlikdə gülmək üçün darıxdığım insanlar var.",
"Xoşbəxtliyi səndə tapan sənindir, üstəlik qonaq.",
"Çox sev, amma bəyənmirsənsə məcbur etmə!",
"O  qədər  gözəl gülürdü ki, sevməsəm ziyan olacaqdı.",
"və  insan insana yoldaş olmalı yaralarını sağalatmalı",
"Məzarlıq, əsəb  uğruna peşman olanlarla dolu",
"Eşq külək  kimidir görməzsən ama hiss edə bilərsən.",
"tərəzi  var ölçü var , hərşeyin bir vaxtı var",
"Yanıltmasın səni masum baxışlar, bəzılarını şeytan ayaqdə alqışlar...",
"həyat sabahı gözləyəcək qədər uzun deyil",
"Yaxşılar əsla itirməz , itirilir.",
"görməzden gəldiyin sevgiyə möhtac qalman diləyiylə",
"Kaşki ağıl vermək yerinə hüzur versəniz",
"Heç bilmədiyim o qoxunu çox özləyirəm",
"𝑌𝑎𝑥𝑠̧𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠𝑒𝑑𝑒 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜̈𝑧ə𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ənə",
"𝐻𝑒𝑐̧𝑘𝑖𝑚 ℎ𝑒𝑐̧𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚𝑒𝑧  𝑔𝑖𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟, 𝑞𝑎𝑙𝑎𝑛 𝑜̈𝑧𝑢̈𝑛𝑢̈",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡𝚤𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘",
"Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑑𝑢𝑞𝑙𝑎𝑟𝚤𝑛𝚤𝑧𝚤  𝑒𝑠̧𝑖𝑑𝑒𝑛 𝑏𝑖𝑟𝑖𝑦𝑙ə 𝑘𝑒ç𝑖𝑟𝑖𝑛",
"𝐺ö𝑛𝑙ü𝑛ü𝑧ə  𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑔̆ı 𝑏𝑖𝑙𝑠𝑖𝑛",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 𝑑𝑒 𝑏𝑢𝑟𝑎𝑥ı𝑏  𝑔𝑖𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝑌𝑎𝑥𝑠̧𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠ə𝑑ə 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏𝑢𝑟𝑎𝑥𝚤𝑟𝑎𝑚  𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
"𝑁ə 𝑖ç𝑖𝑚𝑑ə𝑘𝑖 𝑘𝑢̈𝑐̧ə𝑙ə𝑟ə 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁ə 𝑑ə 𝑐̧𝑜̈𝑙𝑑ə𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",                  
"𝐴𝑟𝑡ı𝑞 ℎ𝑒ç𝑏𝑖𝑟 ş𝑒𝑦 ə𝑣𝑣ə𝑙𝑘𝑖 𝑘𝑖𝑚𝑖 𝑑𝑒𝑦𝑖𝑙 𝐵𝑢𝑛𝑎 𝑚ə𝑛𝑑ə 𝑑𝑎𝑥𝑖𝑙ə𝑚",                
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜̈𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ə𝑛ə",                 
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑌𝑎𝑥𝑠̧𝚤𝑦𝑎𝑚 𝑑𝑒𝑠ə𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑞, 𝑜 𝑘ə𝑑ə𝑟 𝑥ə𝑏ə𝑟𝑠𝑖𝑧 𝑚ə𝑛𝑑ə𝑛", 
"𝐸𝑙ə 𝑔𝑜̈𝑧ə𝑙 𝑏𝑎𝑥𝑡ı 𝑘𝑖 𝑞ə𝑙𝑏𝑖 𝑑ə 𝑔ü𝑙üşü 𝑞ə𝑑ə𝑟 𝑔𝑜̈𝑧ə𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
"𝑀ə𝑠𝑎𝑓ə𝑙ə𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒𝑦𝑖𝑙, İç𝑖𝑚𝑑ə 𝐸𝑛 𝐺ü𝑧ə𝑙 𝑌𝑒𝑟𝑑ə𝑠ə𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜̈𝑦ü𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖ç𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟",
"𝐻𝑒𝑐̧𝑘𝑖𝑚 ℎ𝑒𝑐̧𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚ə𝑧 𝑔𝑒𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟  𝑞𝑎𝑙𝑎𝑛 𝑜̈𝑧𝑢̈𝑛𝑢̈",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘",              
"𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑞𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",
"𝐻ə𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙ə𝑛 𝑑𝑒𝑦𝑖𝑙 𝑞ı𝑦𝑚ə𝑡 𝑏𝑖𝑙ə𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎə𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
"𝑉𝑒𝑟𝑖𝑙ə𝑛 𝑑ə𝑦ə𝑟𝑖𝑛 𝑛𝑎𝑛𝑘𝑜𝑟𝑢 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎə𝑙𝑙𝑜𝑙𝑢𝑟",
"𝑀ə𝑠𝑎𝑓ə 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁ə ℎə𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛ə 𝑑ə 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑥𝑎𝑛",                
"𝐻ə𝑦𝑎𝑡 𝑖rəl𝑖𝑦ə 𝑏𝑎𝑥ı𝑙𝑎𝑟𝑎𝑞 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦ə  𝑏𝑎𝑥𝑎𝑟𝑎𝑞 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 ,  𝑔𝑒𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝐵𝑖𝑟 𝑀𝑜̈𝑐𝑢̈𝑧ə𝑦ə 𝐸ℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟 𝑖𝑑𝑖 𝐻ə𝑦𝑎𝑡 𝑆ə𝑛𝑖 𝑄𝑎𝑟şı𝑚𝑎 Çı𝑥𝑎𝑟𝑑ı",
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣ə 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑢̈𝑟ə𝑦𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏𝑜̈𝑦ü𝑘 𝑏𝑖𝑟                    𝑦𝑜𝑟𝑔̆𝑢𝑛𝑙𝑢𝑞 𝑣𝑎𝑟",
"𝑄ə𝑙𝑏𝑖 𝑔𝑜̈𝑧ə𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑ə𝑛 𝑦𝑎ş ə𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
"𝐻ə𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑑𝑖𝑦𝑖 𝑦𝑒𝑟𝑑ə 𝑚ə𝑛𝑑ə 𝑏𝑖𝑡𝑑𝑖𝑚 𝑑ə𝑦𝑖ş𝑑𝑖𝑛 𝑑𝑒𝑦ə𝑛𝑙ə𝑟𝑖𝑛 ə𝑠ə𝑟𝑖𝑦ə𝑚",
"𝐺ü𝑣ə𝑛𝑚ə𝑘 𝑠𝑒𝑣𝑚ə𝑘𝑑ə𝑛 𝑑𝑎ℎ𝑎 𝑑ə𝑦ə𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
"İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠ə𝑏𝑟𝑙ə  𝑔𝑜̈𝑧𝑙ə𝑑𝑖𝑦𝑖𝑛 ℎ𝑒𝑟 ş𝑒𝑦 𝑢̈𝑐̧𝑢̈𝑛 𝑥𝑒𝑦𝑖𝑟𝑙𝑖 𝑏𝑖𝑟 𝑥ə𝑏ə𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜̈𝑦𝑢̈𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖𝑐̧𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟 ",
"Ö𝑙𝑚ə𝑘 𝐵𝑖𝑟 ş𝑒𝑦 𝑑𝑒y𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑞 𝑞𝑜𝑟𝑥𝑢𝑛𝑐",
"𝐻ə𝑟𝑘ə𝑠𝑖𝑛 𝑏𝑖𝑟 𝑘𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑ə 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",
"𝐺ü𝑐𝑙ü 𝑔ö𝑟ü𝑛ə 𝑏𝑖𝑙ə𝑟ə𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛           𝑦𝑜𝑟𝑔̆𝑢𝑛𝑎𝑚",
"𝐻ə𝑦𝑎𝑡 𝑛ə 𝑔𝑒𝑑ə𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟 𝑛ə𝑑ə 𝑖𝑡𝑖𝑟𝑑𝑖𝑦𝑖𝑛𝑖𝑧 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟",                   
"𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢."
)	

@dejavu.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in dejavu.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await dejavu.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await dejavu.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@dejavu.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎Adminlər Siyahısı♕︎"
    async for x in event.dejavu.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ↯ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)


@dejavu.on(events.NewMessage(pattern='^/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@dejavu.on(events.NewMessage(pattern="^/usta ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in dejavu.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await dejavu.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in dejavu.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await dejavu.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

usta = ('Buda kimmiş də miş miş👀😁😍','🙄👉🤲Aağil','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 


@dejavu.on(events.NewMessage(pattern='/offline'))
async def handler(event):
  if str(event.sender_id) not in Config.Dejavu:
    return await event.reply("__Sən mənə sahib deyilsən!__")
  await event.reply('**Bot İşləyir Narahat olmayın**\n\n╭━━━╮ \n╰╮╭╮┃╱╱╭╮\n╱┃┃┃┣━━╋╋━━┳╮╭┳╮╭╮\n╱┃┃┃┃┃━╋┫╭╮┃╰╯┃┃┃┃\n╭╯╰╯┃┃━┫┃╭╮┣╮╭┫╰╯┃\n╰━━━┻━━┫┣╯╰╯╰╯╰━━╯\n╱╱╱╱╱╱╭╯┃\n╱╱╱╱╱╱╰━╯',
                    buttons=(
    [Button.url('DegGixM','https://t.me/DegGixM'),
	   Button.url('Aliyev Ali','https://t.me/MUCVE_M')],
    ),
    link_preview=False)

print(">> Bot işləyir narahat olmayın.\n\n@DejavuTeam & @DejavuSuopport Məlumat almaq üçün <<")
dejavu.run_until_disconnected()