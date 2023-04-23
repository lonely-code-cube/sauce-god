import discord
from discord import app_commands, Embed
from discord.ext import commands
from core import error
from core.utils import read_config
from bot import BaseBot

import aiohttp

config = read_config()


class HAnime(commands.Cog):
    def __init__(self, bot: BaseBot, session: aiohttp.ClientSession):
        self.bot = bot
        self.session = session

    @commands.group(description="Search hanimes and more", invoke_without_command=True)
    @commands.is_nsfw()
    async def hanime(self, ctx: commands.Context, *, name: str):
        pass


async def setup(bot):
    session = aiohttp.ClientSession(loop=bot.loop)
    await bot.add_cog(HAnime(bot, session))