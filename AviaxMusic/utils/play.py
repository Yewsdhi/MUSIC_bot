from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import pytgcalls
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityAudio,
                                                  LowQualityVideo,
                                                  MediumQualityAudio,
                                                  MediumQualityVideo)
from typing import Union
from pyrogram import Client, filters 
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
import asyncio
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from pytube import YouTube
from config import user, dev, call, logger, logger_mode, botname, appp
from bot import OWNER_ID
from CASERr.daty import get_call, get_userbot, get_dev, get_logger, del_userbot, del_call, get_devss
from pyrogram import Client
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from io import BytesIO
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
import asyncio
import aiohttp
import re
from CASERr.CASERr import devuser, devchannel, devgroup, casery, source, group
from typing import Union
from pyrogram.types import Message

ddd_FOLDER = "/root/ddd"
os.makedirs(ddd_FOLDER, exist_ok=True)


playlist = {}
hossamm = []
vidd = {}
miii = {}
playing = {} 
usera = {}
user_mentio = {}
coun = {}
view = {}
thu = {}
channel_nam = {}
videoi = {}
video_duratio = {}

async def Call(bot_username, message):
    hoss = await get_call(bot_username)
    @hoss.on_stream_end()
    async def stream_end_handler1(client, update: Update):
        if not isinstance(update, StreamAudioEnded):
            return        
        await change_stream(bot_username, update.chat_id, client, message)

async def join_assistant(client, hoss_chat_user, user):
        join = None
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          print()
          return
        try:
          await user.join_chat(str(hos_link))
          join = True
        except Exception as e:
          pass
        return join    

channel_source = "aasdadasds"
gr = "aasdadasds"

async def pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, owner_id, channel_source, gr, playlist):
    bot_username = client.me.username
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    photo_path = f"/root/ddd/{videoid}_{owner_id}.png"
    
    if os.path.isfile(photo_path):
        photo = photo_path
    else:
        try:
            response = requests.get(useram)
            img = Image.open(BytesIO(response.content))
        except Exception as e:
            print(f"Error loading images: {e}")
            return None
        try:
            image1 = changeImageSize(1280, 720, img)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(10))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            draw = ImageDraw.Draw(background)
            box_size = (500, 500)
            box_position = (40, 100)
            box_image = Image.new("RGBA", box_size, (255, 255, 255, 0))
            box_draw = ImageDraw.Draw(box_image)
            box_draw.ellipse([(0, 0), box_size], outline="white", width=5)       
            me = await client.get_me()
            bot_username = me.username
            OWNER_ID = await get_dev(bot_username)        
            wxyz = await client.get_chat(OWNER_ID)
            CAR = wxyz.username
            vvv = wxyz.photo.big_file_id
            wxy = await client.download_media(vvv)
            inner_image = Image.open(wxy)
            inner_image = inner_image.resize((450, 480))
            box_image.paste(inner_image, (10, 10))  
            background.paste(box_image, box_position)   
            font_large = ImageFont.truetype("font.ttf", 75)
            font_small = ImageFont.truetype("font.ttf", 35)
            font_middle = ImageFont.truetype("font.ttf", 45)
            draw.text((550, 80), "PLAYING ELITALY", fill="white", font=font_large)
            draw.text((550, 220), f"{thum}", fill="white", font=font_middle)
            draw.text((550, 370), f"Duration: {video_duration} Mins", fill="white", font=font_small)
            draw.text((550, 420), f"Views: {views}", fill="white", font=font_small)
            draw.text((550, 470), f"Channel: {channel_name} Mins", fill="white", font=font_small)
            background.save(photo_path)
        except Exception as e:
            pass
        photo = photo_path
    button = [
        [InlineKeyboardButton(text="ᎬŃᎠ", callback_data="stop"),
         InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data="resume"),
         InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data="pause")],
        [InlineKeyboardButton(text="ᏟᎻᎪΝΝᎬᏞ", url=soesh),
         InlineKeyboardButton(text="ᏀᎡϴႮᏢ", url=gr)],
        [InlineKeyboardButton(text="آلُــــجـ|𝐄𝐥𝐢𝐭𝐚𝐥𝐲|ـآحــــڊ", url="https://t.me/I_X_J")],
        [InlineKeyboardButton(text="اضف البوت الى مجموعتك ✅", url=f"https://t.me/{bot_username}?startgroup=True")]
    ]    
    if count == 0: 
        await message.reply_photo(photo=photo, caption=f'Starting Playing Now\n\nSong Name : {thum}\nDuration Time : {video_duration}\nBy : {user_mention}', reply_markup=InlineKeyboardMarkup(button))
        await client.send_message(logger, f"**╭──── • ◈ • ────╮\n\nAdd Song To Play\n\n⌁ |Song Name : `{thum}`\nDuration Time : {video_duration}\nBy : {user_mention}\n\n╰──── • ◈ • ────╯**", disable_web_page_preview=True)
    else:
        await message.reply_photo(photo=photo, caption=f'Add Track To Playlist » {count}\n\nSong Name : {thum}\nDuration Time : {video_duration}\nBy : {user_mention}', reply_markup=InlineKeyboardMarkup(button))


async def join_assistant(client, hoss_chat_user, user):
        join = None
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          print()
          return
        try:
          await user.join_chat(str(hos_link))
          join = True
        except Exception as e:
          pass
        return join 

async def join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views):
    file_path = audio_file
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    audio_stream_quality = HighQualityAudio()
    video_stream_quality = HighQualityVideo()
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) 
              if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
        hossamm.append(file_path)
        count = 0
        await pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
        Done = True
    except NoActiveGroupCall:
        h = await join_assistant(client, group_id, userbot)
        if h:
            try:
                await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
                hossamm.append(file_path)
                Done = True
            except Exception:
                pass
    except AlreadyJoinedError:
        if group_id not in playlist:
            playlist[group_id] = []
            vidd[group_id] = []
            miii[group_id] = []
            coun[group_id] = []
            usera[group_id] = []
            videoi[group_id] = []
            video_duratio[group_id] = []
            channel_nam[group_id] = []
            thu[group_id] = []
            view[group_id] = []
            user_mentio[group_id] = []
        if group_id not in playlist[group_id]:
            playlist[group_id].append(file_path)
            vidd[group_id].append(vid)
            miii[group_id].append(mi)
            user_mentio[group_id].append(user_mention)
            usera[group_id].append(useram)
            videoi[group_id].append(videoid)
            video_duratio[group_id].append(video_duration)
            channel_nam[group_id].append(channel_name)
            thu[group_id].append(thum)
            view[group_id].append(views)
        if group_id in playlist:
            count = len(playlist[group_id])
            coun[group_id].append(count)
        await pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
    except TelegramServerError:
        await client.send_message(message.chat.id, "**حدث خطأ في الخادم...**")
    except Exception as e:
       pass
    return False

async def change_stream(bot_username, chat_id, client, message):
    hoss = await get_call(bot_username)
    if chat_id in playlist and playlist[chat_id] and vidd and vidd[chat_id] and miii and miii[chat_id] and coun and coun[chat_id] and user_mentio and user_mentio[chat_id] and usera and usera[chat_id] and videoi and videoi[chat_id] and video_duratio and video_duratio[chat_id] and channel_nam and channel_nam[chat_id] and thu and thu[chat_id] and view and view[chat_id]:
        next_song = playlist[chat_id].pop(0)
        vid = vidd[chat_id].pop(0)
        mi = miii[chat_id].pop(0)
        count = coun[chat_id].pop(0)
        user_mention = user_mentio[chat_id].pop(0)    
        useram = usera[chat_id].pop(0)    
        videoid = videoi[chat_id].pop(0)    
        video_duration = video_duratio[chat_id].pop(0)    
        channel_name = channel_nam[chat_id].pop(0)    
        thum = thu[chat_id].pop(0)    
        views = view[chat_id].pop(0)    
        user_mention = user_mention   
        count = count
        useram = useram
        videoid = videoid
        video_duration = video_duration
        channel_name = channel_name
        thum = thum
        views = views
        file_path = next_song 
        vid = vid      
        mi = mi      
        try:
            audio_stream_quality = HighQualityAudio()
            video_stream_quality = HighQualityVideo()
            hossamm.clear()
            stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
            await hoss.change_stream(chat_id, stream)
            hossamm.append(file_path)
            await pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
        except Exception as e:
            pass
    else:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception as e:
            await message.reply_text("يعم فوق مفيش حاجه شغاله اصلا 😂")

DOWNLOAD_FOLDER = "/root/downloads"
joined_groups = set()
mamno = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
@Client.on_message(filters.command(["تشغيل", "شغل", "فيد", "فيديو", "video", "play"], ""), group=57655580)
async def play_audio(client, message):
    group_id = message.chat.id
    text = None
    if message.reply_to_message:
        if "v" in message.command[0] or "ف" in message.command[0]:
            vid = True
        else:
            vid = None
    else:
        try:
            text = message.text.split(None, 1)[1]
        except IndexError:
            name = await client.ask(
                chat_id=message.chat.id,
                text="ارسل اسم او رابط الي تريد تشغيله.",
                reply_to_message_id=message.id,
                filters=filters.user(message.from_user.id),
                timeout=200
            )
            text = name.text
    if text is None:
        return
    if text in mamno:
        return await message.reply_text("**عذرا لا يمكنني تشغيل هذا**")
    if "v" in message.command[0] or "ف" in message.command[0]:
        vid = True
    else:
        vid = None
    try:
        mm = await message.reply_text("جاري التشغيل انتظر 🚦")
        playing.setdefault(group_id, []).clear()
        playing[group_id].append(message.from_user.id)
    except Exception as e:
        playing[group_id].append(5993309733)
    if group_id not in joined_groups:
        chat_info = await client.get_chat(group_id)
        invite_link = chat_info.invite_link or await message.reply("لا يمكن العثور على رابط الدعوة.")
        if invite_link:
            try:
                await user.join_chat(invite_link)
                joined_groups.add(group_id)
            except Exception:
                pass
    try:
        user_mention = f"{message.from_user.mention}"
    except Exception as e:
        user_mention = "ՏΌႮᎡᏟᎬ ᎬᏞ ᎥͲᎪᏞY"
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    if not mi["search_result"]:
        return await message.reply("لم يتم العثور على نتائج.")
    video_info = mi["search_result"][0]
    mo = video_info["link"]
    mio = mi["search_result"]
    videoid = video_info["id"]
    title = video_info["title"]
    channel_name = mio[0]["channel"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    video_duration = video_info.get("duration", "0")
    views = video_info.get("views", "غير متوفر")
    videoid = video_info.get("id", "غير متوفر")
    useram = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    audio_file = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp4")
    if os.path.exists(audio_file):
        await mm.delete()
        bot_username = client.me.username
        c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views)
        if not c:
            return
        return 
    opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": audio_file,
        "quite": True,
    }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(mo, download=True)
        audio_file = ytdl.prepare_filename(ytdl_data)
    await mm.delete()
    bot_username = client.me.username
    c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views)
    if not c:
        return

@Client.on_message(filters.command(["مين شغل","م شغل","مين مشغل"], ""), group=5880)
async def playingy(client, message):
        chat_id = message.chat.id
        bot_username = client.me.username
        for hos in playing[chat_id]:
          user = await client.get_users(hos)
          user_mention = user.mention()
          await message.reply_text(f"{user_mention} هذا الشخص من قام بالتشغيل 🌿♥️ ")


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

 
@Client.on_callback_query(
    filters.regex(pattern=r"^(pause|skip|stop|resume)$")
)
async def admin_risghts(client: Client, CallbackQuery):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "pause":
        try:
         await hoss.pause_stream(chat_id)
         await CallbackQuery.answer("تم ايقاف التشغيل موقتا .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم ايقاف التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا ❌", show_alert=True)
         await CallbackQuery.message.reply_text(f"لا يوجد شئ قيد التشغيل الان 🚦")
    if command == "resume":
        try:
         await hoss.resume_stream(chat_id)
         await CallbackQuery.answer("تم استكمال التشغيل .", show_alert=True)
         await CallbackQuery.message.reply_text(f"تم إستكمال التشغيل بواسطه {CallbackQuery.from_user.mention} ")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"لا يوجد شئ قيد التشغيل الان 🚦")
    if command == "stop":
        try:
         await hoss.leave_group_call(chat_id)
        except:
          pass
        await CallbackQuery.answer("تم انهاء التشغيل بنجاح ☕🎧 .", show_alert=True)
        await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم انهاء التشغيل بواسطه**")
       
@Client.on_message(filters.command(["اسكت", "ايقاف"], "") & filters.group, group=55646568548)
async def ghuser(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     try:    	
      await hoss.leave_group_call(message.chat.id)
      await message.reply_text("حاضر سكت اهو🚦" )
     except Exception as e:
      await message.reply_text("لا يوجد شئ قيد التشغيل الان 🎧")
    else:
      return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🎧")

@Client.on_message(filters.command(["اسكت", "ايقاف"], "") & filters.channel, group=5564656568548)
async def gh24user(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    try:    	
        await hoss.leave_group_call(message.chat.id)
        await message.reply_text("حاضر سكت اهو🚦")
    except Exception as e:
        await message.reply_text("لا يوجد شئ قيد التشغيل الان 🎧")
 
@Client.on_message(filters.command(["تخطي", "/skip"], "") & filters.group, group=5864548)
async def skip2(client, message):
    group_id = message.chat.id
    bot_username = client.me.username 
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        chat_id = message.chat.id
        ho = await message.reply_text("**جاري تخطي التشغيل**") 
        await change_stream(bot_username, chat_id, client, message)
        await ho.delete()
    else:
        return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🚦")

@Client.on_message(filters.command(["تخطي", "/skip"], "") & filters.channel, group=5869864548)
async def ski25p2(client, message):
    chat_id = message.chat.id
    bot_username = client.me.username 
    ho = await message.reply_text("**جاري تخطي التشغيل**") 
    await ho.delete()
    await change_stream(bot_username, chat_id, client, message)
    
@Client.on_message(filters.command(["توقف", "وقف"], "") & filters.group, group=58655654548)
async def sp2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري توقف التشغيل**") 
     try:    	
      await hoss.pause_stream(chat_id)
      await ho.edit_text("حاضر سكت اهو🚦")
     except Exception as e:
      await ho.edit_text("لا يوجد شئ قيد التشغيل الان 🎧")
    else:
     return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🎧")

@Client.on_message(filters.command(["توقف", "وقف"], "") & filters.channel, group=5866555654548)
async def s356p2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري توقف التشغيل**") 
    try:    	
     await hoss.pause_stream(chat_id)
     await ho.edit_text("حاضر سكت اهو🚦")
    except Exception as e:
     await ho.edit_text("لا يوجد شئ قيد التشغيل الان 🎧")
     
@Client.on_message(filters.command(["كمل"], "") & filters.group, group=5866564548)
async def s12p2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري استكمال التشغيل**") 
     try:    	
      await hoss.resume_stream(chat_id)
      await ho.edit_text("تم استكمال التشغيل ☕🍁")
     except Exception as e:
      await ho.edit_text("لا يوجد شئ قيد التشغيل الان 🎧")
    else:
     return await message.reply_text(f"يجب انت تكون ادمن للقيام بذلك 🎧")

@Client.on_message(filters.command(["كمل"], "") & filters.channel, group=645866564548)
async def s12p582(client, message):
    chat_id = message.chat.id
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    ho = await message.reply_text("**جاري استكمال التشغيل**") 
    try:    	
     await hoss.resume_stream(chat_id)
     await ho.edit_text("تم استكمال التشغيل ☕🍁")
    except Exception as e:
     await ho.edit_text("لا يوجد شئ قيد التشغيل الان 🎧")


#..................................................بحث يوتيوب.................................................................

@Client.on_message(filters.command("بحث",prefixes=""),group=592231800844)
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/search needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text(" searching")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"Song: {results[i]['title']}\n"
            text += f"Duration: {results[i]['duration']}\n"
            text += f"Views: {results[i]['views']}\n"
            text += f"Channel: {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
