import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Use to load environment variable
load_dotenv()

# Load environment variables
TOKEN = os.getenv('TOKEN')

# Specify the bot (subclass of Client) as Cinnamon
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '#', help_command=None)
        
    async def on_ready(self): 
        print(f'{bot.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == bot.user:
            return
        # Register commands to work with on_message
        await bot.process_commands(message)
    
    # Overriding the default error handler to save the error logs
    async def on_error(self, event, *args, **kwargs):
        with open('error.log', 'a') as f:
            if event == 'on_message':
                # Since on_message take only 1 argument so args[0] should be expected to be that argument.
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise discord.DiscordException

    @commands.command(help = 'Show a basic syntax')
    async def syntax(self, context):
        """
        get the basic syntax for each 
        """
        await context.send("Syntax: #(Available commands) [...](arguments).\n Example: #get-report-due-date 2\nFor available commands, please type #help")

    @commands.command()
    async def customized_help(self):
        pass



# Main script
# Create a bot
bot = Bot()

# Load cogs's functionality into Cinnamon
for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #-3 to remove .py

# Get the token to run Cinnamon
bot.run(TOKEN)