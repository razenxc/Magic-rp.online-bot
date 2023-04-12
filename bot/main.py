import disnake
from disnake.ext import commands

import os
from bot.misc import Environment

def start() -> None:
    bot = commands.Bot(
        intents=disnake.Intents.all(),
        command_prefix="/",
        help_command=None,
    )
    for group in [
        'commands',
        'events'
    ]:
        for filename in os.listdir(f'./bot/{group}'):
            if filename.endswith('.py'):
                bot.load_extension(f"bot.{group}.{filename[:-3]}")
    bot.run(Environment.DISCORD_BOT_TOKEN)