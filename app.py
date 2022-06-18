import GPUtil
import platform
import time
from ast import For
from multiprocessing.connection import wait
from cpuinfo import get_cpu_info
from multiprocessing import freeze_support
import os
import sys
import colorama
from colorama  import Fore,Back,Style
from http import client
from turtle import color
from unicodedata import name
import discord
import json
import os
from discord.ext import commands
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
info = get_cpu_info()
cpu = info['brand_raw']
gpus = GPUtil.getGPUs()
for gpu in gpus:
    gpu_name = gpu.name
intents = discord.Intents.default()
intents.message_content = True
with open('setting/config.json') as config:
    data = json.load(config)
    prefix = data["prefix"]
    script = data["script"]
    lo1 = data["urliconembed1"]
    namehub = data["namehub"]
    com = data["commands"]

client = discord.Client(intents=intents)
clear()
clear()
tokens = input("Give Me Token Bot:")
@client.event
async def on_ready():
    clear()
    clear()
    print(Fore.CYAN+"="*40, "EZCode-Community", Fore.CYAN+"="*40)
    print(Fore.BLUE+f' [INFO-CPU]: {cpu}\n',Fore.LIGHTBLUE_EX+f'[INFO-GPU]: {gpu_name}\n',Fore.GREEN+f'[INFO-BOT]: True, Name: {client.user}')
    print(Fore.CYAN+"="*98)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}{com}'):
        embed = discord.Embed(color=0x000000, timestamp=discord.utils.utcnow())
        embed1 = discord.Embed(color=0x43eb34, timestamp=discord.utils.utcnow())
        embed.title = f'{namehub}'
        embed.description = f"**Script Bot!**\nPls Check Your DMs"
        embed.set_footer(text='© 2022 EzCode Made by MrBo!', icon_url=f'{lo1}')
        embed1.title = f'{namehub}'
        embed1.description = f"**Script Bot!**\n```lua\n{script}```"
        embed1.set_footer(text='© 2022 EzCode Made by MrBo!', icon_url=f'{lo1}')
        await message.channel.send(embed=embed)
        await message.author.send(embed=embed1)

client.run(tokens)
