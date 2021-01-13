from discord.ext import commands
from pymongo import MongoClient
from database import db

class Questions (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.faqs = db["FAQs"]

    @commands.command(name = 'FAQs', help = 'Get FAQs')
    async def list_faqs(self, context): 
        cursor = self.faqs.find({})
        for document in cursor:
            order = document['order#']
            question = document['question']
            await context.send(f'Question #{order}: {question}\n')
    

    @commands.command(name = 'add-questions', help = 'Add a question to FAQs', hidden = True)
    @commands.is_owner()
    async def add_questions(self, context, question):
        size = self.faqs.count_documents({})
        data = {'order#': size + 1, 'question': question}
        self.faqs.insert_one(data)
        await context.send('New question accepted!')

    @commands.command(name = 'delele-a-question', help = 'Delete a question', hidden = True)
    @commands.is_owner()
    async def del_questions(self, context):
        await  context.invoke(self.bot.get_command('FAQs'))
        await context.send('Please choose a question to delete! Or type \'cancel\' to stop!')

       # check function
        def check(message):
            if message.lower() == 'cancel':
                return True
            try:
                index = int(message)
                return index > 0 and index < self.faqs.count_documents({})
            except Exception:
                return False

        while True:
            choice = self.bot.wait_for('message', check = check)

            if choice is not None:
                if choice.lower() == 'cancel':
                    return
                query = {'#order': int(choice)}
                self.faqs.delete_one(query)
                break
            else:
                await context.send('Invalid index. Try again!')

def setup(bot):
    bot.add_cog(Questions(bot))
    print('Cog Question added!')


