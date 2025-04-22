import os
import discord

from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

#Load environment
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

