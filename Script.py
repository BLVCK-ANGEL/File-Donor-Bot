class script(object):
    START_TXT = """<b> 𝗛𝗲𝗹𝗹𝗼 {},
𝗠𝘆 𝗡𝗮𝗺𝗲 𝗶𝘀 <a href=https://t.me/{}>{}</a>, 𝗜 𝗰𝗮𝗻 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗙𝗶𝗹𝗺𝘀 𝗮𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀 😊</b>"""
    HELP_TXT = """<b>𝗛𝗲𝘆 {}
𝗛𝗲𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗛𝗲𝗹𝗽 𝗳𝗼𝗿 𝗺𝘆 𝗖𝗼𝗺𝗺𝗮𝗻𝗱.</b>"""

    ABOUT_TXT = """<b>✯ 𝗠𝘆 𝗡𝗮𝗺𝗲: {}
✯ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿: AɴᴏɴʏᴍᴏᴜS    
✯ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ 𝗗𝗮𝘁𝗮𝗕𝗮𝘀𝗲: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ 𝗕𝗼𝘁 𝗦𝗲𝗿𝘃𝗲𝗿: <a href='https://railway.app'>Rᴀɪʟᴡᴀʏ</a>
✯ 𝗕𝘂𝗶𝗹𝗱 𝗦𝘁𝗮𝘁𝘂𝘀: v2.7.1 [ Sᴛᴀʙʟᴇ ]</b>"""
    
    SOURCE_TXT = """<b>𝙽𝙾𝚃𝙴:
- 𝗧𝗵𝗶𝘀 𝗶𝘀 𝗮𝗻 𝗮 𝗼𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁.
- 𝗦𝗼𝘂𝗿𝗰𝗲 - <a href="https://github.com/BLVCK-ANGEL/File-Donor-Bot">ʜᴇʀᴇ</a></b>"""
        
    MANUELFILTER_TXT = """𝗛𝗘𝗟𝗣: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>𝗡𝗢𝗧𝗘:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """𝗛𝗘𝗟𝗣: <b>𝙱𝚄𝚃𝚃𝙾𝙽𝚂</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>𝗡𝗢𝗧𝗘:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """𝗛𝗘𝗟𝗣: <b>𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁</b>
<b>𝗡𝗢𝗧𝗘: 𝙵𝙸𝙻𝙴 𝙸𝙽𝙳𝙴𝚇</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>𝗡𝗢𝗧𝗘: 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """𝗛𝗘𝗟𝗣: <b>𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>𝗡𝗢𝗧𝗘:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """𝗛𝗘𝗟𝗣: 𝙴𝚇𝚃𝚁𝙰 𝙼𝙾𝙳𝚄𝙻𝙴𝚂
<b>𝗡𝗢𝗧𝗘:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""

    ADMIN_TXT = """𝗛𝗘𝗟𝗣: 𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝚂
<b>𝗡𝗢𝗧𝗘:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """𝗛𝗲𝗹𝗹𝗼 {},
𝗧𝗵𝗶𝘀 𝗶𝘀 𝗡𝗼𝘁 𝗬𝗼𝘂𝗿 𝗠𝗼𝘃𝗶𝗲 𝗼𝗿 𝗦𝗲𝗿𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁,
𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗬𝗼𝘂𝗿❜𝘀..."""

    OLD_ALRT_TXT = """𝗛𝗲𝘆 {},
𝗬𝗼𝘂𝗿 𝗮𝗿𝗲 𝘂𝘀𝗶𝗻𝗴 𝗼𝗻𝗲 𝗼𝗳 𝗠𝘆 𝗼𝗹𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲,
𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝘁𝗵𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗔𝗴𝗮𝗶𝗻."""

    CUDNT_FND = """𝗜 𝗖𝗼𝘂𝗹𝗱𝗻❜𝘁 𝗙𝗶𝗻𝗱 𝗔𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗥𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 {}
𝗗𝗶𝗱 𝗬𝗼𝘂 𝗠𝗲𝗮𝗻 𝗔𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝗧𝗵𝗲𝘀𝗲❓"""

    I_CUDNT = """<b>𝗦𝗼𝗿𝗿𝘆 𝗡𝗼 𝗙𝗶𝗹𝗲𝘀 𝘄𝗲𝗿𝗲 𝗙𝗼𝘂𝗻𝗱 𝗙𝗼𝗿 𝗬𝗼𝘂𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """𝗜 𝗖𝗼𝘂𝗹𝗱𝗻❜𝘁 𝗙𝗶𝗻𝗱 𝗔𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗥𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 {}.
𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗵𝗲𝗰𝗸 𝘁𝗵𝗲 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗼𝗻 𝗚𝗼𝗼𝗴𝗹𝗲 𝗼𝗿 𝗜𝗠𝗗𝗕..."""

    MVE_NT_FND = """𝗠𝗼𝘃𝗶𝗲 𝗼𝗿 𝗦𝗲𝗿𝗶𝗲𝘀 𝗡𝗼𝘁𝗙𝗼𝘂𝗻𝗱 𝗶𝗻 𝗗𝗮𝘁𝗮𝗕𝗮𝘀𝗲..."""

    TOP_ALRT_MSG = """𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗙𝗼𝗿 𝗠𝗼𝘃𝗶𝗲 𝗼𝗿 𝗦𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗗𝗮𝘁𝗮𝗕𝗮𝘀𝗲...""" 

    MELCOW_ENG = """<b>𝗛𝗲𝗹𝗹𝗼 {} 😍, 𝗔𝗻𝗱 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 {} 𝗚𝗿𝗼𝘂𝗽 ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ 𝙾𝚆𝙽𝙴𝚁 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : AɴᴏɴʏᴍᴏᴜS """

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

𝗔𝗳𝘁𝗲𝗿 𝟭𝟬 𝗠𝗶𝗻𝘂𝘁𝗲𝘀 𝗧𝗵𝗶𝘀 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗮𝗹𝗹𝘆 𝗗𝗲𝗹𝗲𝘁𝗲𝗱

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Uncharted

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> <code>{file_name}</code>

<b>
╭─────── • ◆ • ───────╮
🔅 Rᴇᴛʀᴏ Mᴏᴅᴇ :  <a href="https://t.me/addtheme/Retrov2">Aᴘᴘʟʏ</a>       🔅
╰─────── • ◆ • ───────╯

=========== • ✠ • ===========
▫️ ᴇɴᴊᴏʏ ᴛʜᴇ Cɪɴᴇᴍᴀ ᴏʀ Sᴇʀɪᴇꜱ
▫️ ʙᴇғᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀɴʏ ғɪʟᴇs 
  ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ sᴀᴍᴘʟᴇ ᴠɪᴅᴇᴏs..
=========== • ✠ • ===========</b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:</b>

🏷 𝚃𝚒𝚝𝚕𝚎: <a href={url}>{title}</a>
🎭 𝙶𝚎𝚗𝚛𝚎𝚜: {genres}
📆 𝚈𝚎𝚊𝚛: <a href={url}/releaseinfo>{year}</a>
🌟 𝚁𝚊𝚝𝚒𝚗𝚐: <a href={url}/ratings>{rating}</a> / 10
🎙️ 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜: <code>{languages}</code>
🎭 𝙲𝚊𝚜𝚝: {cast}      
🌐 𝙲𝚘𝚞𝚗𝚝𝚛𝚒𝚎𝚜: <code>{countries}</code>

🗣 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝗲𝗱 𝗕𝘆: <b>{msg.from_user.mention}</b>"""
    
    ALL_FILTERS = """
<b>𝗛𝗲𝘆 {}, 𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗠𝘆 𝗧𝗵𝗿𝗲𝗲 𝘁𝘆𝗽𝗲𝘀 𝗼𝗳 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 </b>"""
    
    GFILTER_TXT = """
<b>𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗚𝗹𝗼𝗯𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿𝘀. 𝗚𝗹𝗼𝗯𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝘀𝗲𝘁 𝗯𝘆 𝗕𝗼𝘁 𝗔𝗱𝗺𝗶𝗻𝘀 𝘄𝗵𝗶𝗰𝗵 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗼𝗻 𝗮𝗹𝗹 𝗚𝗿𝗼𝘂𝗽𝘀.</b>
    
𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>𝗙𝗶𝗹𝗲 𝗦𝘁𝗼𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗙𝗲𝗮𝘁𝘂𝗿𝗲 𝗪𝗵𝗶𝗰𝗵 𝘄𝗶𝗹𝗹 𝗖𝗿𝗲𝗮𝘁𝗲 𝗮 𝗦𝗵𝗮𝗿𝗲𝗮𝗯𝗹𝗲 𝗹𝗶𝗻𝗸 𝗼𝗳 𝗮 𝗦𝗶𝗻𝗴𝗹𝗲 𝗼𝗿 𝗠𝘂𝗹𝘁𝗶𝗽𝗹𝗲 𝗙𝗶𝗹𝗲𝘀.</b>

𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████─────────██████████████─██████████████─██████─────────██████████─████████──████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░██─██░░░░██──██░░░░██─
─██████░░██████─██░░██████████─██░░██─────────██░░██████████─██░░██████████─██░░██─────────████░░████─████░░██──██░░████─
─────██░░██─────██░░██─────────██░░██─────────██░░██─────────██░░██─────────██░░██───────────██░░██─────██░░░░██░░░░██───
─────██░░██─────██░░██████████─██░░██─────────██░░██████████─██░░██████████─██░░██───────────██░░██─────████░░░░░░████───
─────██░░██─────██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██───────────██░░██───────██░░░░░░██─────
─────██░░██─────██░░██████████─██░░██─────────██░░██████████─██░░██████████─██░░██───────────██░░██─────████░░░░░░████───
─────██░░██─────██░░██─────────██░░██─────────██░░██─────────██░░██─────────██░░██───────────██░░██─────██░░░░██░░░░██───
─────██░░██─────██░░██████████─██░░██████████─██░░██████████─██░░██─────────██░░██████████─████░░████─████░░██──██░░████─
─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░██─██░░░░██──██░░░░██─
─────██████─────██████████████─██████████████─██████████████─██████─────────██████████████─██████████─████████──████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

                                     
                                                                     █▄▄ █▄█   █▄▄ █░░ █░█ █▀▀ █▄▀   ▄▀█ █▄░█ █▀▀ █▀▀ █░░
                                                                     █▄█ ░█░   █▄█ █▄▄ ▀▄▀ █▄▄ █░█   █▀█ █░▀█ █▄█ ██▄ █▄▄  """
    
