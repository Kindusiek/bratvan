import discord
from discord.ext import commands


class Przywitalnia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        kanał = discord.utils.get(member.guild.channels, id=971129089236828210) #id kanału w którym bot wita nowego użytkownika.
        rola = discord.utils.get(member.guild.roles, id=917189023611645983) #id roli danej na start na serwerze.
        embed=discord.Embed(title="*** Nowy użytkownik *** <a:nezuko_jump:975544381346033704> ", description=f"** {member.mention} miło cię widzieć z nami! <a:pika:904487212048068648>  **", color=0x9500a8)
        embed.set_author(name="Bratvan", icon_url= "https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg" )
        embed.set_footer(text=" Baw się dobrze! ")
        await member.add_roles(rola)
        await kanał.send(embed=embed)

def setup(client):
    client.add_cog(Przywitalnia(client))