import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix=".")

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member, reason="Brak Powodu"):
        kanal = discord.utils.get(member.guild.channels, id=983144218463707146) #id kanału wysyłającego log o kicknięciu użytkownika z serwera.
        embed=discord.Embed(title="** Użytkownik wyrzucony <a:eevee:980462371237675048> **", description=f"** {member.mention} Został wyrzucony <a:chilling:980080512318197760> **", color=0x9500a8)
        embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
        embed.add_field(name="Powodem było:", value=f"{reason}", inline=True)
        await member.kick(reason=reason)
        await kanal.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed=discord.Embed(title="** Error❗ **", description='**Użyj komendy .kick, podaj osobę oraz powód w " " aby wyrzucić użytkownika. **', color=0xff0000)
            embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
            embed.add_field(name="Przykład:", value='.kick @użytkownik "Udostępnianie treści niezgodnych z regulaminem"' , inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(kick(client))