import discord.ext.commands as commands
import discord

# Fun(ネタコマンド系) cog
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Fun(bot))