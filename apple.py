import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
one = STRING
two = STRING2
three = STRING3
four = STRING4
five = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


aip = ""
bip = ""
cip = ""
dip = ""
eip = ""
fip = ""
gip = ""
hip = ""
iip = ""
jip = ""

que = {}

DENGU_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_atgk():
    global aip
    global bip
    global cip
    global dip
    global eip
    global fip
    global gip
    global hip
    global iip
    global jip
    if one:
        session_name = str(one)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[1]•")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 1")
            await aip.start()
            botme = await aip.get_me()
            await aip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            aip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[1]•")
        pass
        session_name = "startup"
        aip = TelegramClient(session_name, a, b)
        try:
            await aip.start()
        except Exception as e:
            pass
            
            if two:
        session_name = str(two)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[2]•")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 2")
            await bip.start()
            botme = await bip.get_me()
            await bip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            bip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[2]•")
        pass
        session_name = "startup"
        bip = TelegramClient(session_name, a, b)
        try:
            await bip.start()
        except Exception as e:
            pass
            
            if three:
        session_name = str(three)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[3]•")
        cip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 3")
            await cip.start()
            botme = await cip.get_me()
            await cip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            cip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[3]•")
        pass
        session_name = "startup"
        cip = TelegramClient(session_name, a, b)
        try:
            await cip.start()
        except Exception as e:
            pass
            
            if four:
        session_name = str(four)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[4]•")
        dip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 4")
            await cip.start()
            botme = await cip.get_me()
            await dip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            dip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[4]•")
        pass
        session_name = "startup"
       dip = TelegramClient(session_name, a, b)
        try:
            await dip.start()
        except Exception as e:
            pass
            
            if five:
        session_name = str(five)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[5]•")
        eip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 5")
            await eip.start()
            botme = await eip.get_me()
            await eip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            eip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[5]•")
        pass
        session_name = "startup"
       dip = TelegramClient(session_name, a, b)
        try:
            await eip.start()
        except Exception as e:
            pass
            
            if six:
        session_name = str(six)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[6]•")
        fip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 6")
            await fip.start()
            botme = await fip.get_me()
            await fip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            fip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[6]•")
        pass
        session_name = "startup"
       dip = TelegramClient(session_name, a, b)
        try:
            await fip.start()
        except Exception as e:
            pass
            
            if seven:
        session_name = str(seven)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[7]•")
        fip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 7")
            await fip.start()
            botme = await fip.get_me()
            await gip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            gip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[7]•")
        pass
        session_name = "startup"
       gip = TelegramClient(session_name, a, b)
        try:
            await fip.start()
        except Exception as e:
            pass
            
            if eight:
        session_name = str(eight)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[8]•")
        fip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 8")
            await gip.start()
            botme = await gip.get_me()
            await gip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            gip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[8]•")
        pass
        session_name = "startup"
       gip = TelegramClient(session_name, a, b)
        try:
            await fip.start()
        except Exception as e:
            pass
            
            if ninth:
        session_name = str(ninth)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[9]•")
        fip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 9")
            await hip.start()
            botme = await hip.get_me()
            await hip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            hip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[9]•")
        pass
        session_name = "startup"
       hip = TelegramClient(session_name, a, b)
        try:
            await hip.start()
        except Exception as e:
            pass
            
            if tenth:
        session_name = str(tenth)
        print("𝗥𝗘𝗖𝗘𝗜𝗩𝗘𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[10]•")
        fip = TelegramClient(StringSession(session_name), a, b)
        try:
            print("🐩 Starting Client 10")
            await iip.start()
            botme = await iip.get_me()
            await iip(functions.channels.JoinChannelRequest(channel="@Dengu_Support"))
            botid = telethon.utils.get_peer_id(botme)
            DENGU_USERS.append(botid)
        except Exception as e:
            iip = "dengu"
            print(e)
            pass
    else:
        print("ಠ_ಠ 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 •[10]•")
        pass
        session_name = "startup"
       iip = TelegramClient(session_name, a, b)
        try:
            await iip.start()
        except Exception as e:
            pass
            
