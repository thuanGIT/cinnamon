import discord
from discord import channel
from discord.ext import commands
from pymongo import MongoClient
import os
import help

CONNECTION_URL = os.getenv("CONNECTION_URL")
cluster = MongoClient(CONNECTION_URL)
db = cluster["PHYS122"]
faqs = db["FAQs"]

class Questions (commands.Cog):
    def _init_(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = help.MyHelpCommand()
        bot.help_command.cog = self

    @commands.command(name = 'add-questions', help = 'add a question to FAQs')
    @commands.is_owner()
    async def add_questions(self, context, question):
        size = faqs.count_documents({})
        data = {'order#': size + 1, 'question': question}
        faqs.insert_one(data)
        await context.channel.send('New question accepted!')

    @add_questions.error
    async def del_questions_error(self, context, error):
        if isinstance(error, commands.NotOwner):
            await context.channel.send("You are not authorized for adding a question!")



    @commands.command(name = 'FAQs', help = 'get the FAQs')
    async def list_faqs(self): 
        cursor = await faqs.find({})
        for document in cursor:
            order = document['order#']
            question = document['question']
            print(f'Question #{order}: {question}\n')
    

    @commands.command(name = 'delele-a-question')
    @commands.is_owner()
    async def del_questions(self, context):
       pass
        
    @del_questions.error
    async def del_questions_error(self, context, error):
        if isinstance(error, commands.NotOwner):
            await context.send("You are not authorized for deleting a question!")


    @commands.command(name = 'get-extension', help = 'ask for an extension on a report')
    async def get_extension(self, context):
        await context.send("I cannot help you. Please message Jamie on Canvas!")

def setup(bot):
    bot.add_cog(Questions(bot))
    print('Cog Question added!')


