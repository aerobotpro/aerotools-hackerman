import discord #Discord py
#from pokedex import pokedex
from random import randint, choice
import requests
import asyncio
# SECRET TOKEN
token = "NjQ5MDAzNTkwMjU3NzM3NzM5.XidEKg.atVk82YNbnr50KFlRvjQwBgycbA"

client=discord.Client() #DEFINES CLIENT OBJECT

prefix = "xyz." # Here's your prefix!

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

# ASYNCHRONOUS DEFINITIONS/SEQUENCE BEGINS

# ON_READY():    
@client.event # "Called when the client is done preparing the data received from Discord."
async def on_ready():# "Usually after login is successful and the Client.guilds and co. are filled up."
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))

    #SETTING RICH PRESENCE
    activity = discord.Activity(name="tests happen!", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    
   
#ON_MESSAGE():    
@client.event # "Called when a Message is created and sent."
async def on_message(message):
    if message.author == client.user:
        return

    
    
    if message.content.startswith("test.matrix"):
        query = message.content.replace(f"{message.content.split()[0]} ", "")
        await message.delete()
        q_list = query.split()
        art_list = []
        for x in range(0, len(q_list)):
            r = requests.get(f"http://artii.herokuapp.com/make?text={q_list[x]}")
            art_list.append(
                f"""
```css
{r.text}
```

"""
                )
        this = ""
        for x in range(0, 1455):
            this = this + str(choice(abc))
        m = await message.channel.send(f"**{this}**")
        
        for x in range(0, 15):
            this = ""
            for x in range(0, 1455):
                this = this + str(choice(abc))
            await m.edit(content=f"**{this}**")
            await asyncio.sleep(.5)
            await m.edit(content=f"**{choice(art_list)}**")
            await asyncio.sleep(.5)
            for x in range(0, 5):
                this = ""
                for x in range(0, 1455):
                    this = this + str(randint(0, 1))
                await m.edit(content=f"**{choice(art_list)}**")
                await asyncio.sleep(.5)
                await m.edit(content=f"**{this}** <@632636197784649758>")

def prefix(string):
    return f"{prefix}{string}"


client.run(token)   #INITIALIZE CLIENT/CONNECTION 
