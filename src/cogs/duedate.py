from discord.ext import commands
from pymongo import MongoClient
from database import db


class DueDate(commands.Cog, name = 'Due Date'):
    ''' Deal with due dates of reports and pre labs'''
    def __init__(self, bot):
        self.bot = bot
        # Connect to MongoDB cluster
        self.dueDate = db["dueDate"]

    @commands.command(name = 'report-due-date', help = 'Get the due date for a report')
    # Return the current due date
    # arg  is the report #
    async def report_due_date(self, context, number: int):
        # A report # is valid (valid if it is less than or equal to the current one)
        # A document in MongoDB is represented as a dictionary in pymongo
        dates = self.dueDate.find_one({"report#": number})
        result = 'Sorry I found no due dates. \nEither your report # is invalid or you are a little ahead!'
        bonus = ''
        if dates != None:
            result = 'Due date for report ' + str(dates["report#"]) + ' is ' + dates["due-date"]
            bonus = '\nPrelab ' + str(dates["report#"] + 1) + ' is also due on that day! Make sure you submit it!' 
        await context.channel.send(result + bonus)
        
    @commands.command(name = 'set-report-due-date', help = 'Set the due date for a report', hidden = True)
    @commands.is_owner()
    # args[0] = report #
    # args[1] = due date of report #
    async def set_report_due_date(self,context, *args):
        # try update the database. If not found, insert the new document
        query = {"report#": args[0]}
        check = self.dueDate.update_one(query, {"$set": {"due-date": args[1]}}, upsert = True)
        result = "Successully added"
        
        if check.matched_count != 0:
            result = "Report " + args[0] + " is already given due date. Update accepted!"

        await context.channel.send(result)

    @commands.command(name = 'get-extension', help = 'Ask for an extension on a report')
    async def get_extension(self, context):
        await context.send("I cannot help you. Please message Jamie on Canvas!")
        
def setup(bot):
    bot.add_cog(DueDate(bot))
    print('Cog DueDate added!')      