import disnake
from disnake.ext import commands
from typing import Union

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.response.send_message(
                embed=disnake.Embed(
                    title="Command On Cooldown",
                    description=f"Повторіть спробу через {round(error.retry_after, 2)} секунд",
                    color=0xff0000
                ),
                ephemeral=True
            )

def setup(bot):
    bot.add_cog(ErrorHandling(bot))