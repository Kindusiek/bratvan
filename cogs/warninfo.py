import discord
import sqlite3
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix=".")

class warninfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def winfo(self, ctx, member: discord.Member):
        kanal = discord.utils.get(member.guild.channels, id=971130194423316520) #id kanału wysyłającego log o ilości warnów użytkownika na serwerze.
        db = sqlite3.connect("warns.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM warns WHERE guild_id = {ctx.author.guild.id} AND user_id = {member.id}")
        wynik = cursor.fetchall()
        nm = 1
        if wynik:
            for warn in wynik:
                    embed=discord.Embed(title="** Warny **", description=f"** Warn {nm} użytkownika {member.mention} za {warn[2]}. **", color=0xff0000)
                    embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
                    await kanal.send(embed=embed)
                    nm += 1
        else:
            embed=discord.Embed(title="** Warny **", description=f"** {member.mention} nie posiada warnów. Gratulacje! **", color=0xff0000)
            await kanal.send(embed=embed)
            cursor.close()
            db.close()

def setup(client):
    client.add_cog(warninfo(client))