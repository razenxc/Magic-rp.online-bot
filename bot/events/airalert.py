import disnake
from disnake.ext import commands, tasks

import random
import aiohttp
from datetime import datetime
from bot.misc import Config, Environment


class RaidAlert(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @tasks.loop(seconds=40)
    async def raid_alert(self) -> None:
        url = 'https://alerts.com.ua/api/states'
        headers = {'X-API-Key': Environment.ALERTS_API_TOKEN}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response_data = await response.json()
                response_time = datetime.strptime(response_data['last_update'][0:19], '%Y-%m-%dT%H:%M:%S')

        embed = disnake.Embed(
            title="📢 Повітряні тривоги",
            description="🔴 - Повітряна тривога\n🟢 - Немає повітряної тривоги\n⚪ - Немає інформації\nㅤ",
            colour=Config.embed_color
        )
        embed.set_image(url=f"https://alerts.com.ua/map.png?{random.randint(1, 100000)}")
        embed.set_footer(text=f"{response_time.strftime('%H:%M   %d-%m-%Y')}")

        alert_regions = [region['name'] for region in response_data['states'] if region['alert']]
        if alert_regions:
            embed.add_field(
                name="Повітряна тривога у:",
                value='\n'.join([f'🚨{region}' for region in alert_regions]) if len(alert_regions) < 25 else "🚨 Вся "
                                                                                                           "Україна"
            )

        channel = self.bot.get_channel(Config.alert_channel_id)
        message = await channel.history(limit=1).flatten()

        if message:
            await message[0].edit(embed=embed)
        else:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.raid_alert.start()


def setup(bot):
    bot.add_cog(RaidAlert(bot))