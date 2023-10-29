import discord
from redbot.core import commands

class DiscordID(commands.Cog):
    """Get the discord ID of a user."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def discordid(self, ctx, member: discord.Member):
        """Get the discord ID of a user."""
        embed = discord.Embed(description=str(member.id), color=await ctx.embed_color())
        await ctx.send(embed=embed)
