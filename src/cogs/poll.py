import discord
from discord.ext import commands
import help

class Poll(commands.Cog):
    def _init_(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = help.MyHelpCommand()
        bot.help_command.cog = self


    @commands.command(name = "run-poll")
    async def run_poll(self, context):
        pass


def setup(bot):
    bot.add_cog(Poll(bot))
    print('Cog Poll added!')      