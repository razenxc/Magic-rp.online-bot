import disnake
from disnake.ext import commands

from bot.misc import Config

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"{self.bot.user} is ready and online!")
        await self.bot.change_presence(
            status=disnake.Status.dnd,
            activity=disnake.Game(f'{Config.bot_presence_title}')
        )

def setup(bot):
    bot.add_cog(Ready(bot))