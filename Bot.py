import os
import discord

from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

#Load environment
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


#make intent / Permissions
intents = discord.Intents.default()

#now allowing intend to perform action/Permissions
intents.message_content = True 

#creating bot command by passing command prefix and its intends
bot = commands.Bot(command_prefix="@",intents=intents)


#making bot online and listen for events
@bot.event
async def on_ready():

    #to sync slash / commands in discord
    await bot.tree.sync()
    #print when bot goes online
    print(f"{bot.user} Online")
    print("---------------------------------------------------------------")


#making bot listen to messages in server
@bot.event
async def on_message(msg):

    #checking is message is not sent by bot itself
    if msg.author.id != bot.user.id :
        await msg.channel.send(f"Fuck you {msg.author.mention}")


#for create slash command use tag
#discord.interaction use to get user info who ran command
@bot.tree.command(name="greet",description="say Hello")
async def greet(interaction:discord.Interaction):

    try:

        username = interaction.user.mention

        await interaction.response.send_message(f"Hello {username}")

    except Exception as error:
        print(f"Error = {error}")



#this will make bot online
bot.run(TOKEN)