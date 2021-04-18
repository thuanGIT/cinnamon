from discord.ext import commands
import sys

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): 
        print(f'{self.bot.user} has connected to Discord!')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content
        # Check if the sender is the bot itself
        if message.author == self.bot.user:
            return
        elif not content.startswith('#'): 
            await message.channel.send("Let me notify Jamie! Please wait a little...", delete_after = 0.5)
        
        # Register commands to work with on_message
        # Only use this in @bot.event. If placed in a listener, do not manually call this.
        # await self.bot.process_commands(message)
    
    # Overriding the default error handler to save the error logs
    # Won't take any effect as said by the documentation
    # @commands.Cog.listener()
    # async def on_error(self, event, *args, **kwargs):
    #     with open('error.log', 'a') as f:
    #         # Since on_message take only 1 argument (message) so args[0] should be expected to be that argument.
    #         f.write(f'Unhandled message: {args[0]}\n')

    #Overwrite on_command_error 
    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        type_help = '\nType \'#help\' to see available commands and instructions.'
        if isinstance(error, commands.CommandNotFound):
            await context.send("No such command found!" + type_help)
        elif isinstance(error, commands.BadArgument):
            await context.send("Syntax Error!" + type_help)
        elif isinstance(error, commands.NotOwner):
            await context.send("You are not authorized for deleting a question!" + type_help)
        else: 
            print(error)
            await context.send("Opps! Something happens!" + type_help)
    
    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Cinnamon disconnected for some reason.")

    @commands.Cog.listener()
    async def on_resumed(self):
        print("Cinnamon is back online.")

def setup(bot):
    bot.add_cog(Event(bot))