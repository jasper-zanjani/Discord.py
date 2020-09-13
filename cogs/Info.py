import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def getchannel(self, ctx):
        channels = [c.name for c in ctx.guild.channels if type(c) is discord.TextChannel]
        print(channels)

def setup(client):
    client.add_cog(Info(client))