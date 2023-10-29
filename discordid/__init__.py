from .discordid import DiscordID

async def setup(bot):
    await bot.add_cog(DiscordID(bot))
