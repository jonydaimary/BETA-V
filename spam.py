#discord bot made by marcos
#Red_GT - youtube
#<@498378677512437762> - discord

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
            await asyncio.sleep(2)
            await bot.say(SecretCocoSpam)
            
            
@bot.command(pass_context=True)
async def spam2(ctx, count: int, *, SecretCocoSpam: str):
    if ctx.message.author.id == "498378677512437762":
        await bot.delete_message(ctx.message)
        for i in range(count):
            await asyncio.sleep(0.5)
            await bot.say(SecretCocoSpam)
            
 
@bot.command(pass_context=True)
async def spam3(ctx): 
    while True:
        await bot.say("YOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\n") #NOTE - you need the \n (new lines)
        await bot.say("YOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\n")
        await bot.say("YOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\n")
        await bot.say("YOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\n")
        await bot.say("YOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\nYOURTEXTHERE\n")



   @commands.command()
    async def boobs(self, ctx):
        """WARNING: NSFW command. Gets pictures of boobs."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("boobs")
        em = discord.Embed(color=0xf9e236, title="Boobs :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

##BOT TOKEN##
bot.run(os.getenv('Token')) 
