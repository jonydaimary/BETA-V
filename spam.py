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
bot = commands.Bot(description="marcos Bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)


bot.remove_command('help')


##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online")
    


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
            
@bot.command(pass_context=True, no_pm=True, aliases=["yan"])
async def yandere(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["pantsu", "swimsuits", "dress", "breasts", "animal ears", "open shirt", "bra", "no bra", "cameltoe", "loli"\
				" thighhighs", "cleavage", "nipples", "ass", "bikini", "naked", "pussy", "panty pull", "see through", "underboob"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://yande.re/post/index.json?limit={}&tags={}".format(limit, message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = x["file_url"]
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From yande.re, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

            
bot.run(os.getenv('Token'))

