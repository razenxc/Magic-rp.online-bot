import random
import disnake
from disnake.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Rolls a dice.")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dice(self, ctx, sides: int = 6):
        if sides < 1:
            await ctx.response.send_message("The dice must have at least 1 side.", ephemeral=True)
        else:
            result = random.randint(1, sides)
            embed = disnake.Embed(
                title=f"The dice rolled {result}!",
                color=disnake.Color.green()
            )
            await ctx.response.send_message(embed=embed, ephemeral=False)

def setup(bot):
    bot.add_cog(Dice(bot))
