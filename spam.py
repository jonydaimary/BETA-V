##IMPORTS## 
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp	

##PREFIX##
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
bot = commands.Bot(description="marcos Official Bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)
client = commands.Bot(description="marcos Official Bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)


bot.remove_command('help')


##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
 
#######################
## Made by Coco#6429 ##
#######################
@bot.command(pass_context=True)
async def spam(ctx, count: int, *, SecretCocoSpam: str):
    if ctx.message.author.id == "498378677512437762":
        await bot.delete_message(ctx.message)
        for i in range(count):
            await asyncio.sleep(0.5)
            await bot.say(SecretCocoSpam)
            
            
@bot.command(pass_context=True)
async def spam2(ctx, count: int, *, SecretCocoSpam: str):
    if ctx.message.author.id == "498378677512437762":
        await bot.delete_message(ctx.message)
        for i in range(count):
            await asyncio.sleep(0.5)
            await bot.say(SecretCocoSpam)
            
########
@client.command(pass_context = True)
async def lovedetect(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('```Proper usage is \n!!lovedetect @user1 @user2```')


            
bot.run(os.getenv('Token'))
client.run(os.getenv('Token')) 

