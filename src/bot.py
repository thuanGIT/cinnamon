from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.messages = True
intents.members = True

class Bot(commands.Bot):
    def __init__(self, command_prefix = '#', description = 'PHYSLAB122_BOT', intents = intents, **options):
        super().__init__(command_prefix = command_prefix, description=description,  **options, intents = intents)
        self.email = "thuan.vo@ubc.ca"
        self.lab_channels = {
            "lab03": 796700415293915156,
            "lab12": 796700478523572234
        }


    @commands.command(name = "send_noti", hidden = True)
    @commands.is_owner()
    async def send_notification(self, context, message):
        lab03_channel = discord.utils.get(await message.guild.fetch_channels(), id = self.lab_channels["lab03"])
        lab12_channel = discord.utils.get(await message.guild.fetch_channels(), id = self.lab_channels["lab12"])

        await lab03_channel.send(message.content)
        await lab12_channel.send(message.content)
        

