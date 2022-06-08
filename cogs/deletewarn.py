import discord
import sqlite3
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix=".")

class deletewarn(commands.Cog):
    def _init(self, client):
        self.client = client

    @commands.command()
    @has_permissions(ban_members=True)
    async def delwarn(self, ctx, member : discord.Member, numer: int):
        kanal = discord.utils.get(member.guild.channels, id=971130194423316520) #id kanału wysyłającego log o usunięciu warna danego użytkownika.
        db = sqlite3.connect("warns.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM warns WHERE guild_id = {ctx.author.guild.id} AND user_id = {member.id}")
        wynik = cursor.fetchall()
        nm = 1
        if wynik:
            for warn in wynik:
                if nm == numer:
                    cursor.execute(f"DELETE FROM warns WHERE guild_id = ? AND user_id = ? AND content = ? AND author_id = ? AND time = ?", (warn[0], warn[1], warn[2], warn[3], (warn[4])))
                    embed=discord.Embed(title="** Usunięto warna! ** <a:HyperNeko:975618445737611324>", description=f"** Warn {nm} użytkownika {member.mention} został usunięty! ** <:peepolove:904485997683806250>", color=0xff0000)
                    embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
                    embed.set_footer(text="Oby tak dalej!")
                    await kanal.send(embed=embed)
                    nm += 1
                    db.commit()
                    cursor.close()
                    
    @delwarn.error
    async def delwarn_error(self, ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed=discord.Embed(title="** Error❗ **", description='**Użyj komendy .delwarn, podaj osobę oraz podaj numer warna aby go usunąć! **', color=0xff0000)
            embed.set_author(name="Bratvan", icon_url="https://i.pinimg.com/originals/03/53/94/0353940ff6e7857b38142909ca8bbde2.jpg")
            embed.add_field(name="Przykład:", value='.delwarn @użytkownik 1' , inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(deletewarn(client))