import mysql.connector
import discord

class db:
                    
    def is_guild_in_db(guild):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="pandas420goated",
            database="aerobot"
            )
        
        mycursor = mydb.cursor()            
        guild_id = str(guild.id)
        sql = f"SELECT * FROM guilds WHERE guild_id ='{guild_id}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
            itis = True
        else:
            itis = False
        return itis


    def update_guild(guild):
        d = True
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="pandas420goated",
                database="aerobot"
                )
            mycursor = mydb.cursor()            
            sql = "INSERT INTO guilds"
            " (guild_id, guild_name, avatar_url, guild_description, guild_region, guild_member_count)"
            " VALUES (%s, %s, %s, %s, %s, %s)"
            val = (str(guild.id), guild.name, guild.icon_url, guild.description, guild.region, str(guild.max_members))
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            d = False
        return d
    
    #if message.channel.startswith("")
    #x = await message.channel.create_invite(max_age=0, max_uses=0, reason="Hackerman Profile Invite")
    #update

    
    def update_guild_invite(guild, invite):
        d = True
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="pandas420goated",
                database="aerobot"
                )
            mycursor = mydb.cursor()
            sql = "INSERT INTO guilds"
            " (guild_invite)"
            " VALUES (%s)"
            f" WHERE guild_id ='{str(guild.id)}'"
            val = (str(invite))
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            d = False
        return d

    
    def get_guild_invite(guild, invite):
        try:
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="pandas420goated",
                database="aerobot"
                )
            mycursor = mydb.cursor()        
            d = str()
            mycursor.execute(f"SELECT guild_invite FROM guilds WHERE guild_id ='{str(guild.id)}'")
            d = mycursor.fetchall()
            if len(str(myresult)) < 1:
                d = None
        except Exception as e:
            print(str(e))
            d = None
        return d

        
        
        
            
        
        
        
        
        
        
        
        
