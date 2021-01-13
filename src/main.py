import os
from dotenv import load_dotenv
import bot

# Use to load environment variable
load_dotenv()

# Load environment variables
TOKEN = os.getenv('TOKEN')

# Main script
# Create a bot
bot = bot.Bot()
if __name__ == "__main__":
    # Load cogs's functionality into Cinnamon
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}') #-3 to remove .py


    # Get the token to run Cinnamon
    bot.run(TOKEN)