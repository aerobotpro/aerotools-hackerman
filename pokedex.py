import requests
import discord

class pokedex:
    def pokedex(message):
        q = message.content.split()[1]
        r = requests.get(
            f'https://some-random-api.ml/pokedex?pokemon={str(q)}'
            )
        a = r.json()
        try:
            stats = a['stats']
            family = a['family']
            sprites = a['sprites']
            embed = discord.Embed(title=f"HackerMan Pokedex | {str(a['name'])}",description=" ", url="https://host-info.net/", color=0x8000ff)
            embed.set_author(name=message.author.name + "#" + message.author.discriminator,
                             url='https://host-info.net',
                             icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://host-info.net/cdn/img/pokecord.png")
            embed.add_field(name="__**Name:**__", value="`"+str(a['name'])+"`", inline=False)
            embed.add_field(name="__**Description:**__", value=f"`"+str(a['description'])+"`", inline=False)
            embed.add_field(name="__**Stats:**__", value=f"""
```css
HP: {str(stats['hp'])}
Attack: {str(stats['attack'])}
Defense: {str(stats['defense'])}
Special Attack: {str(stats['sp_atk'])}
Special Defense: {str(stats['sp_def'])}
Speed: {str(stats['speed'])}
----------------------------------------
Total: {str(stats['total'])}
```
""", inline=False)
            evo_line = str("\n")
            for x in range(0, len(family['evolutionLine'])):
                evo_line += str(f"Stage {str(x + 1)}: {family['evolutionLine'][x]}\n")
            embed.add_field(name="__**Family:**__", value=f"""
```css
EvolutionStage: {str(family['evolutionStage'])}
----------------------------------------
EvolutionLine: {evo_line}
```
""", inline=False)
            embed.add_field(name="__**Type:**__", value="`"+str(a['type']).replace("'", "").replace("[", "").replace("]", "")+"`", inline=True)
            embed.add_field(name="__**Species:**__", value="`"+str(a['species']).replace("'", "").replace("[", "").replace("]", "")+"`", inline=True)
            embed.add_field(name="__**Abilities:**__", value="`"+str(a['abilities']).replace("'", "").replace("[", "").replace("]", "")+"`", inline=True)
            embed.add_field(name="__**Size:**__", value=f"`Height: {str(a['height'])} | Weight: {str(a['weight'])}`", inline=True)
            embed.add_field(name="__**Base Experience:**__", value="`"+str(a['base_experience'])+"`", inline=True)
            embed.add_field(name="__**Gender:**__", value="`"+str(a['gender']).replace("'", "").replace("[", "").replace("]", "")+"`", inline=True)
            embed.add_field(name="__**Egg Groups:**__", value="`"+str(a['egg_groups']).replace("'", "").replace("[", "").replace("]", "")+"`", inline=True)

            embed.add_field(name="__**ID:**__", value="`"+str(a['id'])+"`", inline=True)
            embed.add_field(name="__**Generation:**__", value="`"+str(a['generation'])+"`", inline=True)            
            
            embed.add_field(name="__**API Credit:**__", value=f"Pokedex API by [some-random-api.ml](https://some-random-api.ml)", inline=False)
            embed.set_image(url=sprites['animated'])
            embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")



            
        except Exception as d:
            print(d)
            embed = discord.Embed(title=f"Pokedex | Not Found",description=" ", url="https://host-info.net/", color=0x8000ff)
            embed.set_author(name=message.author.name + "#" + message.author.discriminator, url='https://host-info.net', icon_url=message.author.avatar_url)
            embed.add_field(name="__**API Credit:**__", value=f"Pokedex API by [some-random-api.ml](https://some-random-api.ml)", inline=False)
            embed.set_image(url="https://host-info.net/cdn/img/pokecord.png")
            embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")

        return embed    
