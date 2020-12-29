import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        await message.channel.send('Hello!')

client.run('NzkzMDE1OTk4MDEzMjQzMzk0.X-mHsw.6oqak_0NYoDb6N-dfXFM3XPwLmk')