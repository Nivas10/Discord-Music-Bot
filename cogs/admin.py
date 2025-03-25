import discord
from discord.ext import commands

from utils.config import Config
from utils.checks import is_admin

class Admin(commands.Cog):
    """Administrative commands for the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config()

    @commands.command()
    @is_admin()
    async def setprefix(self, ctx, prefix):
        """Sets the command prefix for the server."""
        self.config.set_prefix(ctx.guild.id, prefix)
        await ctx.send(f'Command prefix set to `{prefix}`.')

    @commands.command()
    @is_admin()
    async def getprefix(self, ctx):
        """Gets the command prefix for the server."""
        prefix = self.config.get_prefix(ctx.guild.id)
        await ctx.send(f'Current command prefix: `{prefix}`.')

    @commands.command()
    @is_admin()
    async def setvolume(self, ctx, volume: float):
        """Sets the volume for the bot on the server."""
        if volume < 0 or volume > 1:
            await ctx.send('Volume must be between 0 and 1.')
            return

        self.config.set_volume(ctx.guild.id, volume)
        await ctx.send(f'Volume set to {volume}.')

    @commands.command()
    @is_admin()
    async def getvolume(self, ctx):
        """Gets the volume for the bot on the server."""
        volume = self.config.get_volume(ctx.guild.id)
        await ctx.send(f'Current volume: {volume}.')

    @commands.command()
    @is_admin()
    async def setsources(self, ctx, *sources):
        """Sets the allowed music sources for the server."""
        self.config.set_allowed_sources(ctx.guild.id, list(sources))
        await ctx.send(f'Allowed sources set to: {", ".join(sources)}')

    @commands.command()
    @is_admin()
    async def getsources(self, ctx):
        """Gets the allowed music sources for the server."""
        sources = self.config.get_allowed_sources(ctx.guild.id)
        await ctx.send(f'Allowed sources: {", ".join(sources)}')

    @commands.command()
    @is_admin()
    async def status(self, ctx, *, status: str):
        """Sets the bot's status."""
        await self.bot.change_presence(activity=discord.Game(name=status))
        await ctx.send(f'Status set to: {status}')

    @commands.command()
    @is_admin()
    async def clearqueue(self, ctx):
        """Clears the music queue for the server."""
        # Assuming you have a music cog with a `clear_queue` function
        await ctx.invoke(self.bot.get_cog('Music').clear_queue)
        await ctx.send('Music queue cleared.')

def setup(bot):
    bot.add_cog(Admin(bot))
