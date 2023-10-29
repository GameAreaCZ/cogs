import discord
from redbot.core import commands

class DiscordID(commands.Cog):
    """Get the discord ID of a user."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def discordid(self, ctx, member: discord.Member=None):
        """Get the discord ID of a user."""
        if member is None:
            member = ctx.author
            nazev = ctx.member
        else:
            nazev = ctx.author
        embed = discord.Embed(title=nazev, description=str(member.id), color=await ctx.embed_color())
        await ctx.send(embed=embed)