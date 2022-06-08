import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix=".")

class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, reason="Brak Powodu"):
        kanal = discord.utils.get(member.guild.channels, id=909672042125725726) #id kanału wysyłającego log o zbanowaniu użytkownika z serwera.
        embed=discord.Embed(title="** Użytkownik zbanowany ** <a:PandaConducter:975618383355711588> ", description=f"** {member.mention} Został zbanowany <:PandaSleepCry:975165426931761192> **", color=0x9500a8)
        embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
        embed.add_field(name="Powodem było:", value=f"{reason}", inline=True)
        embed.set_footer(text="Miejmy nadzieję że kiedyś jego zachowanie się poprawi.")
        await member.ban(reason=reason)
        await kanal.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="** Error❗ **", description='**Użyj komendy .ban, podaj osobę oraz powód w " " aby zbanować użytkownika. **', color=0xff0000)
            embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
            embed.add_field(name="Przykład:", value='.ban @użytkownik" "Nie przestrzeganie regulaminu"', inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ban(client))