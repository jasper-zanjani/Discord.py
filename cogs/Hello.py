import discord
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user.name} is ready to go as a cog as well!')

    @commands.command()
    async def hello(self, ctx):
        user = ctx.message.author.name
        embed = discord.Embed(
            title="Hey there!",
            description=f'Hello {user} :grin:'
        )
        # print('Hello world')
        await ctx.send(embed=embed)

    @commands.command()
    async def dmme(self, ctx):
        owner_id = ctx.guild.owner_id
        owner = self.client.get_user(owner_id)
        print(owner_id)
        await owner.send(f'Hey, {ctx.author.name} is in my DMs.. betta handle dat!')
        

def setup(client):
    client.add_cog(Hello(client))