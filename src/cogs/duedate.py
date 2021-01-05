from discord.ext import commands
from pymongo import MongoClient
import os
import help

# Connect to MongoDB cluster
CONNECTION_URL = os.getenv("CONNECTION_URL")
cluster = MongoClient(CONNECTION_URL)
db = cluster["PHYS122"]
dueDate = db["dueDate"]

class DueDate(commands.Cog):
    ''' Deal with due dates of reports and pre labs'''
    def _init_(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = help.MyHelpCommand()
        bot.help_command.cog = self

    @commands.command(name = 'report-due-date', help = 'get the due date for the specified report')
    # Return the current due date
    # arg  is the report #
    async def report_due_date(self, context, number: int):
        db = cluster["PHYS122"]
        dueDate = db["dueDate"]
        
        # A report # is valid (valid if it is less than or equal to the current one)
        dates = dueDate.find_one({"report#": number})
        result = 'Sorry I found no due dates. \nEither your report # is invalid or you are a little ahead!'

        if dates != None:
            result = 'Due date for report ' + str(dates["report#"]) + ' is ' + dates["due-date"]
        await context.channel.send(result)
        
    @commands.command(name = 'set-report-due-date', help = 'set the due date for the specify report')
    @commands.is_owner()
    # args[0] = report #
    # args[1] = due date of report #
    async def set_report_due_date(self,context, *args):
        # try update the database. If not found, insert the new document
        query = {"report#": args[0]}
        check = dueDate.update_one(query, {"$set": {"due-date": args[1]}}, upsert = True)
        result = "Successully added"
        
        if check["matchedCount"] == 0:
            result = "Report " + args[0] + " is already given due date. Update accepted!"

        await context.channel.send(result)
        

    @commands.command()
    async def prelab_due(self, context):
        pass
    @commands.command()
    async def set_prelab_due(self, context):
        pass

def setup(bot):
    bot.add_cog(DueDate(bot))
    print('Cog DueDate added!')      