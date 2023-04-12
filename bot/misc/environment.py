from abc import ABC
from typing import Final
from os import getenv

class Environment(ABC):
    DISCORD_BOT_TOKEN: Final = getenv('DISCORD_BOT_TOKEN')
    ALERTS_API_TOKEN: Final = getenv('ALERTS_API_TOKEN')