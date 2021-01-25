from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.messages = True
intents.members = True

class Bot(commands.Bot):
    def __init__(self, command_prefix = '#', description = 'PHYSLAB122_BOT', intents = intents, **options):
        super().__init__(command_prefix = command_prefix, description=description,  **options, intents = intents)
        self.email = "thuan.vo@ubc.ca"


    @commands.command(name = "send_noti", hidden = True)
    @commands.is_owner()
    async def send_notification(self, context, message):
        pass
        

