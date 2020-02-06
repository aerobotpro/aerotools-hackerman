import discord
from os import mkdir, chmod, remove,rmdir
from sum_sql import db




def add_page(client, guild, fresh_invite):
    res = 0
    try:
        with open("aero-data/html/guild_page.html", "r") as d:
            file = d.read()
    except Exception as e:
        print(str(e))
        res = 1
    access_rights = 0o755    
    #formatting :X
    base = "/var/www/html/discord/hackerman/guilds"
    main_dir = f"{base}/{guild.id}/"
    if fresh_invite != None:
        invite = fresh_invite
    else:
        y = db(guild).get_guild_invite()
        if y != None:
            invite = y
        else:
            invite = "https://discordapp.com/#Lacking_Permission_To_Create_An_Invite!"    
    owner = client.get_user(int(guild.owner_id))
    owner_name = str(owner.name + " #" + str(owner.discriminator))    
    file = file.replace("$guild_owner", str(owner_name))
    file = file.replace("$guild_id", str(guild.id))
    file = file.replace("$guild_member_count", str(len(guild.members)))
    file = file.replace("$guild_name", str(guild.name))
    file = file.replace("$guild_avatar", str(guild.icon_url))
    file = file.replace("$guild_description", str(guild.description))
    file = file.replace("$guild_region", str(guild.region))
    file = file.replace("$guild_invite", str(invite))
    index = str(main_dir + "index.html")
    try:
        mkdir(main_dir, access_rights)
    except Exception as DD:
        pass
    with open(index, "w+") as d:
        d.write(file)
    chmod(index, access_rights)
    return res
    





def add_page_user(client, member):
    res = 0
    try:
        with open("aero-data/html/user_page.html", "r") as d:
            file = d.read()
    except Exception as e:
        print(str(e))
        res = 1
    access_rights = 0o755
    try:
        user = client.get_user(int(member.id))
    except:
        return
    #formatting :X
    file = file.replace("$user_avatar", str(user.avatar_url))
    file = file.replace("$user_id", str(user.id))
    file = file.replace("$user_name", str(user.name + " #" + str(user.discriminator)))
    
    base = "/var/www/html/discord/hackerman/users"
    main_dir = f"{base}/{user.id}/"
    index = str(main_dir + "index.html")
    try:
        mkdir(main_dir, access_rights)
    except Exception as DD:
        pass
    with open(index, "w+") as d:
        d.write(file)
    chmod(index, access_rights)
    return res


def remove_user_page(client, member):
    res = 0
    base = "/var/www/html/discord/hackerman/users"
    main_dir = f"{base}/{member.id}/"    
    try:
        remove(main_dir+"index.html")
        rmdir(main_dir)
    except Exception as e:
        pass
        res = 1
    return res    
    
    
    
    
