from discord.ext import commands
import discord



class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = {'lab03_student': 794843886333722624,
                      'lab12_student': 794843964683190273}
        self.emojis = {'3': '\U0001F602', '12':'\U0001F62D'}
        self.lab_channels = {'lab03': 796700415293915156, 'lab12': 796700478523572234}
        

    @commands.command(name = "run-role-poll", help = 'Run role poll', hidden = True)
    async def run_role_poll(self, context):
        poll_channel = discord.utils.get(self.bot.get_all_channels(), name = 'poll')
        file = discord.File('./assets/UBC.jpg', filename = 'UBC.jpg')
        em = discord.Embed(
            colour = discord.Colour.dark_orange(), 
            description = 'React to my message and I will assign you to your lab channel!')
        em.add_field(name = 'Lab03', value = self.emojis['3'], inline = True) # Add emoji instruction
        em.add_field(name = 'Lab12', value = self.emojis['12'], inline = True)
        em.set_thumbnail(url = 'attachment://UBC.jpg')
        message = await poll_channel.send(embed = em, file = file)
        await message.add_reaction(self.emojis['3'])
        await message.add_reaction(self.emojis['12'])

   
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Check if the reaction is in poll channel
        channel_id = payload.channel_id
        channel = discord.utils.get(self.bot.get_all_channels(), id = channel_id)
        reaction_sender = payload.member
        if channel.name != 'poll' or reaction_sender == self.bot.user or payload.guild_id is None: 
            #Do nothing if the reaction is in channel #poll/the bot itself/private dm
            return

        guild = await self.bot.fetch_guild(payload.guild_id) 
        emoji = payload.emoji
        noti = ''
        role = None
        if emoji.name == self.emojis['3']:
            role = discord.utils.get(await guild.fetch_roles(), id = self.roles['lab03_student']) # Find role by ID
            lab03 = self.bot.get_channel(self.lab_channels['lab03']) # Send a message to guide member to their lab channel
            noti = f'You have been assigned to lab03_student. You may now to go {lab03.mention}.'
        elif emoji.name == self.emojis['12']:
            role = discord.utils.get(await guild.fetch_roles(), id = self.roles['lab12_student'])
            lab12 = self.bot.get_channel(self.lab_channels['lab12'])
            noti = f'You have been assigned to lab12_student. You may now to go {lab12.mention}.'
        else:
            noti = 'Your emoji assigns you to no lab! Might wanna take another choice?'

        await reaction_sender.add_roles(role, reason = 'check in')  # Set role for member that send the emoji
        await channel.send(noti, delete_after = 3.0)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        poll_channel = discord.utils.get(self.bot.get_all_channels(), name = 'poll')
        await poll_channel.send(f'You removed emoji {payload.emoji.name}. Do you want to deselect your role? (y/n)')
        choice = await self.bot.wait_for('message', check = lambda message: message.content.lower().startswith('y')) # Wait for user input
        
        if choice:
            await self.remove_a_role(choice, payload.emoji)

    async def remove_a_role(self, message, emoji):
        reaction_sender = message.author
        role = None
        guild = message.guild
        if emoji.name == self.emojis["3"]:
            role = discord.utils.get(await guild.fetch_roles(), id = self.roles['lab03_student'])
        elif emoji.name == self.emojis["12"]:
            role = discord.utils.get(await guild.fetch_roles(), id = self.roles['lab12_student'])
        
        if role:
            await reaction_sender.remove_roles(role, reason = 'remove emoji')
            await message.channel.purge(limit = 2)

      
    @commands.command(name = 'stop-poll', help = 'Stop all polls', hidden = True)
    async def stop_poll(self, context):
        poll_channel = discord.utils.get(self.bot.get_all_channels(), name = 'poll')
        await poll_channel.purge(limit = 10)

    @commands.command(name = 'remind-role-poll', help = "remind everyone to get role", hidden = True)
    async def remind_poll(self, context):
        general = discord.utils.get(self.bot.get_all_channels(), name = 'general')
        poll_channel = discord.utils.get(self.bot.get_all_channels(), name = 'poll')
        file = discord.File('./assets/remind.jpg', filename ='remind.jpg')
        em = discord.Embed(
            title = "REMINDER!",  
            description = f'For anyone who is not assigned a role, please vote in {poll_channel.mention}',
            color = discord.Color.dark_orange())
        em.set_thumbnail(url = 'attachment://remind.jpg')
        await general.send(embed = em, file = file)
        

def setup(bot):
    bot.add_cog(Poll(bot))
    print('Cog Poll added!')      