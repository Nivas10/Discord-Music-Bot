import discord
from discord.ext import commands

def is_connected():
    """Check if the bot is connected to a voice channel."""
    def predicate(ctx):
        if ctx.voice_client:
            return True
        else:
            raise NotConnected("The bot is not connected to a voice channel.")
    return commands.check(predicate)

def is_admin():
    """Check if the user is an administrator."""
    def predicate(ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        else:
            raise MissingPermissions("You do not have permission to use this command.")
    return commands.check(predicate)