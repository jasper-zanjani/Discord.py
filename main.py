import os
import dotenv
from discord.ext import commands
import discord

dotenv.load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to go!")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 753012365267828837:
        guild = discord.utils.get(bot.guilds, id=payload.guild_id)
        role = discord.utils.get(guild.roles, name='Turtles')
        member = discord.utils.get(guild.members, id=payload.user_id)
        await member.add_roles(role)

    # print(f'guild_id: {payload.guild_id}')
    # print(f'channel_id: {payload.channel_id}')
    # print(f'message_id: {payload.message_id}')
    # print(f'emoji: {payload.emoji.name}')

bot.load_extension('cogs.Hello')
bot.load_extension('cogs.Info')

bot.run(token)
# https://discordapp.com/channels/752642461309993001/752642461754720338/752724862342004777