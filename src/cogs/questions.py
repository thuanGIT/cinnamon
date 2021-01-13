from discord.ext import commands
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
            QA = document["QA"]
            question = QA['question']
            answer = QA['answer']
            await context.send(f'Question #{order}: {question}\n\t->{answer}')
    

    @commands.command(name = 'add-questions', help = 'Add a question to FAQs', hidden = True)
    @commands.is_owner()
    async def add_questions(self, context, question, answer):
        size = self.faqs.count_documents({})
        data = {'order#': size + 1, "QA": {'question': question, 'answer': answer}}
        self.faqs.insert_one(data)
        await context.send('New question accepted!')

    @commands.command(name = 'delele-a-question', help = 'Delete a question', hidden = True)
    @commands.is_owner()
    async def del_questions(self, context):
        await  context.invoke(self.bot.get_command('FAQs'))
        await context.send('\nPlease choose a question to delete! Or type \'cancel\' to stop!')
        while True:
            choice = await self.bot.wait_for('message', check = None)
            print(choice.content)
            if choice is not None:
                if choice.content.lower() == 'cancel':
                    return
                query = {'#order': int(choice.content)}
                delete = self.faqs.delete_one(query)
                if delete:
                    await context.send("Delete successfully!")
                break
            else:
                await context.send('Invalid index. Try again!')

def setup(bot):
    bot.add_cog(Questions(bot))
    print('Cog Question added!')


