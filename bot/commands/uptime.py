import disnake
from disnake.ext import commands

from datetime import timedelta
from time import time

class Uptime(commands.Cog):
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot
        self.start_time = time()

    @commands.slash_command(name="uptime", description="Shows bot uptime")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def uptime(self, inter: disnake.interactions.application_command.ApplicationCommandInteraction) -> None:
        current_time = time()
        difference = int(round(current_time - self.start_time))
        text = str(timedelta(seconds=difference))
        embed = disnake.Embed(color=0x14F803)
        embed.add_field(name="Uptime", value=text)
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Uptime(bot))
