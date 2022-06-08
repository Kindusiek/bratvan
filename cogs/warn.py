import discord
import sqlite3
import time
from discord.ext import commands
from discord.ext.commands import has_permissions
from distutils.log import warn

client = commands.Bot(command_prefix=".")

class warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(ban_members=True)
    async def warn(self, ctx, member : discord.Member, *,reason):
        kanal = discord.utils.get(member.guild.channels, id=971130194423316520) #id kanału wysyłającego log o nadania warna użytkownikowi z serwera.
        embed=discord.Embed(title="** Ktoś dostał warna! **", description=f"**  Użytkownik {member.mention} dostał warna za {reason}! **", color=0xff0000)
        embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
        embed.set_footer(text="Lepiej bądź czujny/a bo następne warny mogą skutkować mutem/kickiem/banem!")
        db = sqlite3.connect('warns.db')
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO warns(guild_id, user_id, content, author_id, time) VALUES(?, ?, ?, ?, ?)", (ctx.author.guild.id, member.id, reason, ctx.author.id, time.time()))
        await kanal.send(embed=embed)
        db.commit()
        cursor.close()
        db.close()

def setup(client):
    client.add_cog(warn(client))