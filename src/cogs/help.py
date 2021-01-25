from discord.ext import commands
import discord

class CommandHelp(commands.Cog, name = 'Help'):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')
        self.clean_prefix = self.bot.command_prefix
        
    # Called when #help is called without argument
    @commands.command(name = "help", help = 'Show avaiable commands.')
    async def send_help(self, context, *command_name):

        if command_name:
            # Assuming there is only 1 passed argument -> command_name
            print(command_name)
            await self.send_command_help(context, command_name)
            return

        em = discord.Embed(
            colour = discord.Colour.dark_orange(), 
            title = 'Available commands',
            description = 'General format: #<Command-name> (optional)[args..]')
        text = f'For detailed information, you can type \'{context.command.name} <command name>\''
        em.set_footer(text = f"P/S: Have fun studying! \U0001F602\n{text}")
        file = discord.File("./assets/help.png", filename="help.png")
        em.set_thumbnail(url = 'attachment://help.png')

        
        # Find a mapping of all registered cogs
        for name, cog in self.bot.cogs.items():
            # Do not show these
            black_list = ["Poll", "Greetings", "Event"]
            if name in black_list:
                continue
            
            value = ""
            for command in cog.get_commands():
                if command.hidden:
                    continue
                # Get the desciption and params dict
                des = command.help if command.help else 'Coming Soon!'
                des = "Description: " + des
                params = " "
                if command.clean_params:
                    for param_name in command.clean_params:
                        params = ("<" + str(param_name) + "> " )
                        # Check if command
                        if param_name == "command_name":
                            params = "(optional)" + params
                
                sig = f"Command_name: {command.name}\n{des}\nSyntax:```{self.clean_prefix}{command.qualified_name} {params}\n```\n"
                value += sig
            em.add_field(name = "For " + name + "\n", value = value, inline = False)
        await context.send(embed = em, file = file, delete_after = 20)


    async def send_command_help(self, context, command_name):
        print(command_name)
        if len(command_name) > 1:
            await context.send("A little too many commands. Just one at a time!")
        else:
            command = self.bot.get_command(command_name[0])
            if command:
                em = discord.Embed(
                    colour = discord.Color.dark_orange(),
                title = command.name,
                description = "Description: "+ command.help)
                params = " "
                if command.clean_params:
                    for param_name in command.clean_params:
                        params = ("<" + str(param_name) + "> " )
                        # Check if command
                        if param_name == "command_name":
                            params = "(optional)" + params
                em.add_field(name = "Syntax: ", value = f"```{self.clean_prefix}{command.qualified_name} {params}```")
                await context.send(embed = em, delete_after = 20)   
            else:
                await context.send("No command found! Type '#help' to see available commands!")
        


def setup(bot):
    bot.add_cog(CommandHelp(bot))
    print('Cog Help added!')