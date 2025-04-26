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
intents.members = True

#creating bot command by passing command prefix and its intends
bot = commands.Bot(command_prefix="!guard ",intents=intents)


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
async def on_message(message):

    #checking is message is not sent by bot
    if message.author.bot: return 
 # Let commands process normally
    await bot.process_commands(message)
    
    # Debug output
    if message.content.startswith(bot.command_prefix):
        print(f"Received possible command: {message.content}")
        print(f"Command interpretation: {bot.get_command(message.content[1:])}")
    
    

#for create slash command use tag
#discord.interaction use to get user info who ran command
@bot.tree.command(name="greet",description="say Hello")
async def greet(interaction:discord.Interaction):

    try:

        username = interaction.user.mention

        await interaction.response.send_message(f"Hello {username}")

    except Exception as error:
        print(f"Error = {error}")



#test command
@bot.command(name="slap")
async def prefix_slap(ctx:commands.Context):
    await ctx.send("I am not sleeping")


#Help Command
@bot.hybrid_command(name="help-commands",description="Show All commands availables",aliases=['!guard '])
async def help_commands(interaction:commands.Context):

    print("Working on 'Help Commands'")

    #defer if commnad is slapsh command
    if isinstance(interaction,discord.Interaction):
        await interaction.response.defer()
        send_method = interaction.followup.send

    else:
        send_method = interaction.send

    embed = await showHelpCommands(interaction)



#server infomation command
@bot.hybrid_command(name="serverinfo",description="Show Server informations",aliases=['!guard '])
async def server_info(interaction:commands.Context):
    
    print(f"Working on Server info command")
    #defer if command is slash command
    if isinstance(interaction,discord.Interaction):
        await interaction.response.defer()
        send_method = interaction.followup.send

    else:
        send_method = interaction.send
        print(f"prefix")

    guild = interaction.guild
    try:

        if not guild:
            return await send_method("command only work in server")

        embed = await showServerInfo(interaction)

    #sending response
        await send_method(embed=embed)
        print(f"sent 'SERVER INFORMATION' ")

    except Exception as error:

        print(f"Error : {error}")





async def showServerInfo(ctx):

    #get guild
    guild = ctx.guild


    #create Server embed
    embed = discord.Embed(
        title=f"Server Information : {guild.name}",
        color=discord.Color.blue()
    )

    
    #if server have icon then also show icon
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)


    #getting owner 
    try:
        owner = guild.owner or await guild.fetch_member(guild.owner_id)
        owner_display = owner.mention
    
    except (discord.NotFound, discord.HTTPException):
        owner_display = f"<@{guild.owner_id} (Not in catch)"


    #now add fields of server infomation 
    embed.add_field(name="Owner", value=owner_display, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Created At", value=guild.created_at.strftime("%b %d %Y"), inline=True)


    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Text Channels", value=len(guild.text_channels), inline=True)
    embed.add_field(name="Voice Channels", value=len(guild.voice_channels), inline=True)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Verification Level", value=str(guild.verification_level).title(), inline=True)

    embed.set_footer(text="------Server Infomation------")

    return embed

async def showHelpCommands():

    embed = discord.Embed(
        title="All Commands",
        color=discord.color.green()
    )

    fields = [
        
    ]







#this will make bot online
bot.run(TOKEN)