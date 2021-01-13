from discord import colour
from discord.ext import commands
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_member_join(self, member):
        poll_channel = discord.utils.get(self.bot.get_all_channels(), name = 'poll')
        em = discord.Embed(
            colour = discord.Colour.dark_orange(),
            title = "Welcome to PHYS122 Lab3/Lab12 Server"
        )
        em.add_field(name = "Your first task", value = f"Please come to {poll_channel.mention} to tell me which lab you are in!")
        await member.send(embed = em, delete_after = 5.0)

def setup(bot):
    bot.add_cog(Greetings(bot))
    print('Cog Greeting added!')