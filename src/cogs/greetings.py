import discord
from discord.ext import commands
import help


class Greetings(commands.Cog):
    def _init_(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = help.MyHelpCommand()
        bot.help_command.cog = self

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.channel.send(f"Welcome {member} to PHYS122 Lab!")

        
    @commands.command()
    async def remind(self, context):
        pass

def setup(bot):
    bot.add_cog(Greetings(bot))
    print('Cog Greeting added!')