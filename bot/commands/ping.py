import disnake
from disnake.ext import commands

from bot.misc import Config

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Відправляє затримку бота.")
    async def ping(self, ctx):
        latency = self.bot.latency * 1000  # Задержка в миллисекундах
        embed = disnake.Embed(
            title="Pong!",
            description=f"Затримка: {latency:.2f} мс.",
            color=Config.ping_embed_color,
        )
        await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))
