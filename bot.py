import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils.config import Config
from utils.errors import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=Config.get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')

@bot.command()
async def load(ctx, extension):
    """Loads a cog."""
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} loaded.')
    except Exception as e:
        await ctx.send(f'Failed to load cog: {e}')

@bot.command()
async def unload(ctx, extension):
    """Unloads a cog."""
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} unloaded.')
    except Exception as e:
        await ctx.send(f'Failed to unload cog: {e}')

@bot.command()
async def reload(ctx, extension):
    """Reloads a cog."""
    try:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} reloaded.')
    except Exception as e:
        await ctx.send(f'Failed to reload cog: {e}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)