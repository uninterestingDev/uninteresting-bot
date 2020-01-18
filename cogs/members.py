import discord
from discord.ext import commands
from utilities import getConfig

class Members(commands.Cog, name='Members'):
    def __init__(self, bot):
        self.bot = bot
        self.config = getConfig()
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if int(self.config['guild']['history_channel']) > 0:
            channel = member.guild.get_channel(int(self.config['guild']['history_channel']))
            if channel != None:
                await channel.send('**Welcome {0.mention} :tada:**'.format(member))
        if self.config['guild']['use_placeholders'] != "0":
            for placeholder in self.config['guild']['use_placeholders'].split(','):
                role = discord.utils.get(guild.roles, id=int(placeholder))
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if int(self.config['guild']['history_channel']) > 0:
            channel = member.guild.get_channel(int(self.config['guild']['history_channel']))
            if channel != None:
                await channel.send('*Bye {0.mention} :sleepy:*'.format(member))

def setup(bot):
    bot.add_cog(Members(bot))