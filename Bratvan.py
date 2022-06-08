import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import os
import sqlite3
import random
import time

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@has_permissions(ban_members=True)
async def pomoc(ctx):
    embed=discord.Embed(title="** Lista dostępnych komend. **", color=0xb80090)
    embed.set_author(name="Bratvan", icon_url= "https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg" )
    embed.add_field(name=".kick", value="wyrzuca użytkownika z serwera.")
    embed.add_field(name=".ban", value="banuje użytkownika z serwera.")
    embed.add_field(name=".graj", value="zmienia status gry bota.")
    embed.add_field(name=".warn", value="warnuje użytkownika na serwerze.")
    embed.add_field(name=".winfo", value="pokazuje warny danego użytkownika.")
    embed.add_field(name=".delwarn", value="usuwa warny danego użytkownika.")
    await ctx.send(embed=embed)

@client.event
async def on_ready():
        db = sqlite3.connect("warns.db")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS warns(guild_id INT, user_id INT, content STR, author_id INT, time INT)")
        cursor.close()
        db.close()
        print("Bratvan działa")
        print("Załadowano database warnów")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="** Error❗ **", description="** Taka komenda nie istnieje! **", color=0xff0000)
        embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
        await ctx.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def weryfikacja(ctx):                                                                          #id roli
    embed=discord.Embed(title="*** Witaj w naszej społeczności! ***", description="** Kliknij ✅ aby być <@&904473302620315668> i w pełni cieszyć się serwerem! **", color=0x00ff11)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 984075767740772432: #id wiadomości
        if payload.emoji.name == '✅':
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = discord.utils.get(guild.roles, id=904473302620315668) #id roli
            await member.add_roles(rola)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 984075767740772432: #id wiadomości
        if payload.emoji.name == '✅':
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = discord.utils.get(guild.roles, id=904473302620315668) #id roli
            await member.remove_roles(rola)


@client.command()
async def graj(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))

@graj.error
async def graj_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nie podałes gry.")






client.run(os.environ["DISCORD_TOKEN"])
