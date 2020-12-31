import discord
import os
#from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

# Use to load environment variable
#load_dotenv()
# Specify the user (here it is Cinnamon)
client = discord.Client()
# Connect to MongoDB cluster
cluster = MongoClient(os.getenv("CONNECTION_URL"))


@client.event
async def on_ready(): 
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#question'):
        question = {"id": message.author.id, "question": message.content.lower().split("#question", 1)[1]}
        db = cluster["PHYS122"]
        collection = db["FAQs"]
        collection.insert_one(question)
        await message.channel.send('Great Question!')

# Get the token to run Cinnamon
client.run(os.getenv('TOKEN'))