##############################################
######### made by marcos.#0290  ##############
##############################################
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


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0xf9fcfc)
client = commands.Bot(description="marcos bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)

client.remove_command('help')



async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='!!help | marcos.#0290', type=2)) 
        await asyncio.sleep(50)
        await client.change_presence(game=discord.Game(name='BETA VERSION')) 
        await asyncio.sleep(50)
        await client.change_presence(game=discord.Game(name='with ' +str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(50)
       
	
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')
    client.loop.create_task(status_task())

	
def is_owner(ctx):
    return ctx.message.author.id == "498378677512437762"	
		

@client.event
async def on_message(message):
    channel = client.get_channel('519791076803084288')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : <@{}> : '.format(message.author.name, message.author.id) + message.content)
    await client.process_commands(message)
		

@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    embed = discord.Embed(color = 0xf9fcfc)
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='*Thanks for Joining our Server Hope you enjoy please respect all members and staff.*',inline = False)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/520159870448566287/524894568072609816/youre_welcome_obama.gif')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='bysoyal2', name='》welcome')
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check Rules and never try to break any one of them', color = 0xf9fcfc)
    embed.add_field(name='__Thanks for joining__', value='*Hope you will be active here.*', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/520159870448566287/524894568072609816/youre_welcome_obama.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)		
	

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'welcome_swagat':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/486489391083159574/520207004334292992/Loading.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await client.send_message(channel, embed=embed)	
		

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'welcome_swagat':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)	
		
		
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = 'dab-log'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == 'dab-log':
          logchannel = channel
          embed = discord.Embed(color=0Xf9fcfc)
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)         
          await client.send_message(logchannel,  embed=embed)	
				


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'dab-log',everyone)

	

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcome(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, 'welcome-swagat',everyone)
			
		
	
@client.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title="meme", color=0XF9FCFC)
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()          
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)		
	
	
@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()           
            embed = discord.Embed(color=0Xf9fcfc) 
            embed.set_image(url=res['message'])  
            embed.title = "{} twitted: {}".format(usernamename, txt)
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")	 
            await client.say(embed=embed)
            
			

		
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
	
		
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(title='User: {}'.format(ctx.message.author.name), color=0Xf9fcfc)
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title='User: {}'.format(user.name), color=0Xf9fcfc)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)
	    
	
@client.command(pass_context = True)
async def announce(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('```Proper usage is \n\n!!announce #channel matter```')
        return
    else:
        if member.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            await client.send_message(channel, msg)
            await client.delete_message(ctx.message)
	
	
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("**You do not have permission to use this command**")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: !!dm [tag person] [msg]")

		
	
@client.command(pass_context = True, aliases=["invite"])
async def botinvite(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Invite dab to your server!", description="[Click to invite dab](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot)" , color=0Xf9fcfc)
      embed.add_field(name="Join dab home server!", value="[Click to join dab server](https://discord.gg/dFM9HG6)")
      embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
      embed.timestamp = datetime.datetime.utcnow()
      await client.say(embed=embed)



@client.command(pass_context = True)
async def test(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Hii bro what supp')
      await client.say('Check your dm ')
	

@client.command(pass_context=True)  
@commands.has_permissions(administrator=True)    
async def kick(ctx,user:discord.member):
    if user.server_permissions.kick_members:
      await client.say('*He is mod/admin and i am unable to kick him/her*')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == 'information-log':
            embed=discord.Embed(title="User kicked!", description="*{0}* is kicked by *{1}*!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)



@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def rolesetup(ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)
    admin_perms = discord.Permissions(ADMINISTRATOR=True)

    await client.create_role(author.server, name="Owner", permissions=admin_perms)
    await client.create_role(author.server, name="Admin", permissions=admin_perms)
    await client.create_role(author.server, name="Moderator", permissions=mod_perms)
    await client.create_role(author.server, name="Friend of Owner")


 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: *{}*".format(message))
    await client.say(":angry:  __*{0} Has Been Warned!*__ :warning: *Reason:{1}* ".format(userName,message))
    pass


@client.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
    await client.add_roles(ctx.message.mentions[0], role)




@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
      await client.say('```The proper usage is \n!!userinfo <@user>```')
      return
    else:
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0Xf9fcfc)
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
      embed.timestamp = datetime.datetime.utcnow()
      embed.set_image(url = user.avatar_url)
      await client.say(embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    join = discord.Embed(description= '%s '%(str(server)),title = '__Server Name__', color=0Xf9fcfc)
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.add_field(name = '__Created__', value = str(time));
    join.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    join.timestamp = datetime.datetime.utcnow()
    return await client.say(embed = join);






@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    if user is None:
      await client.say('```The proper usage is \n!!setnick @user <new nickname```')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == 'information-log':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)
		



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color=0Xf9fcfc)
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text=f"Poll ID: {react_message.id}",)
        embed.timestamp = datetime.datetime.utcnow()
        await client.edit_message(react_message, embed=embed)

	

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == 'information-log':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0xf9fcfc)
            await client.send_message(channel, embed=embed)


@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
      await client.say('Ban list is empty.')
      return
    else:
      await client.unban(ctx.message.server, ban_list[-1])
      await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
      for channel in member.server.channels:
        if channel.name == 'soyal-log':
            embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(ban_list[-1].name, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)


@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)	

@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Ping: {}ms".format(round((t2-t1)*1000)))
			

@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()       
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color=0Xf9fcfc)
            embed.set_image(url=res['message'])
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

	
@client.command(pass_context=True)
async def merrychristmas(ctx, user:discord.Member=None):
    if user is None:
        embed=discord.Embed(title='merry christmas', description=f'I wanna wish {ctx.message.author} Merry Christmas {ctx.message.author}', color=0Xf9fcfc)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/532088532576239647/536425202335219722/tenor.gifw.gif')
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {user} Merry Christmas {user}', color=0Xf9fcfc)
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/532088532576239647/536425202335219722/tenor.gifw.gif')
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    if user.id == ctx.message.author.id:
        await client.say("Goodluck slaping yourself {}".format(ctx.message.author.mention))
    else:
        gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0Xf9fcfc)
        embed.set_image(url=random.choice(gifs))
        await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    if user == None:
        await client.say("```Proper usage is\n\n!!hug <mention a user>```")
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color=0Xf9fcfc)
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)    


@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    if user == None:
        await client.say("```Proper usage is\n\n!!kiss <mention a user>```")
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color=0Xf9fcfc)
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)


@client.command(pass_context=True)
async def joke(ctx):
    embed = discord.Embed(color=0Xf9fcfc)
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await client.say(embed=embed)

		
	
@client.command(pass_context=True, no_pm=True, aliases=["Cat"])
async def cat(ctx):
    try:
        url = "http://shibe.online/api/cats?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Cat {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    except:
        x = await client.say("Sorry, there was an error with the **cat** command")
        await asyncio.sleep(5)
        await client.delete_message(x)    
    	
	
@client.command(pass_context=True, no_pm=True, aliases=["Fox"])
async def fox(ctx):
    try:
        url = "https://randomfox.ca/floof"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Fox {}".format(ctx.message.author.name),)
        embed.set_image(url = data["image"])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    except:
        x = await client.say("Sorry, there was an error with the **fox** command")
        await asyncio.sleep(5)
        await client.delete_message(x)  	
	

@client.command(pass_context=True, no_pm=True, aliases=["Bird"])
async def bird(ctx):
    try:
        url = "http://shibe.online/api/birds?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Bird {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    except:
        x = await client.say("Sorry, there was an error with the **bird** command")
        await asyncio.sleep(5)
        await client.delete_message(x) 
	
	
@client.command(pass_context=True, no_pm=True, aliases=["Dog"])
async def dog(ctx):
    try:
        url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Dog {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    except:
        x = await client.say("Sorry, there was an error with the **dog** command")
        await asyncio.sleep(5)
        await client.delete_message(x)    
	
	
@client.command(pass_context = True, aliases=["server"])
async def serverinvite(ctx):
    await client.say("*Thanks for joining in our server*.... \n https://discord.gg/Dgvq9vK ")


@client.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '519935085739507722':
        await client.say('You should use ``!!checkinvites``')
        return
    if user is None:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = 0xf9fcfc)
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == ctx.message.author:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)
    else:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = 0xf9fcfc)
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == user:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)

	
	
@client.command(pass_context=True)
async def checkinvites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '519935085739507722':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter I')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter II')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter III')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter IV')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter IV role')
        else:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(user.server.roles, name='Inviter I')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name}, You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(user.server.roles, name='Inviter II')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(user.server.roles, name='Inviter III')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(user.server.roles, name='Inviter IV')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter IV role')
    else:
        await client.say('You are not allowed to use this command in this server')
        return 	





@client.command(pass_context=True)
async def inviteb(ctx):
    total_uses=0
    server = ctx.message.channel.server
    invites = await client.invites_from(server)
    invlb = f'Invites of {ctx.message.server.name}\n'
    for invite in invites:
      total_uses += invite.uses
      invlb += f'User: {invite.inviter.name}\nInvites: {invite.uses}\n'
    embed=discord.Embed(color=0xf9fcfc)
    embed.add_field(name='Invites List',value=invlb)
    embed.add_field(name='Total Invites',value=total_uses)
    embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.say(embed=embed)		

	



@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
    await client.send_typing(ctx.message.channel)
    if name is None:
        embed=discord.Embed(description = "Please specify a movie, *eg. %movie Bohemian Rhapsody*", color=0xf9fcfc)
        await client.say(embed=embed)
    key = "4210fd67"
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
    response = requests.get(url)
    x = json.loads(response.text)
    embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = 0xf9fcfc)
    if x["Poster"] != "N/A":
     embed.set_thumbnail(url = x["Poster"])
    embed.add_field(name = "__Title__", value = x["Title"])
    embed.add_field(name = "__Released__", value = x["Released"])
    embed.add_field(name = "__Runtime__", value = x["Runtime"])
    embed.add_field(name = "__Genre__", value = x["Genre"])
    embed.add_field(name = "__Director__", value = x["Director"])
    embed.add_field(name = "__Writer__", value = x["Writer"])
    embed.add_field(name = "__Actors__", value = x["Actors"])
    embed.add_field(name = "__Plot__", value = x["Plot"])
    embed.add_field(name = "__Language__", value = x["Language"])
    embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
    embed.add_field(name = "__Type__", value = x["Type"])
    embed.set_footer(text = "Information from the OMDB API")
    await client.say(embed=embed)

@client.command(pass_context = True)
async def marvel(ctx):
    choices = ['https://media.giphy.com/media/F9hQLAVhWnL56/giphy.gif', 'https://media.giphy.com/media/l4FGrYKtP0pBGpBAY/giphy.gif', 'https://media.giphy.com/media/JzujPK0id34qI/giphy.gif', 'https://media.giphy.com/media/M9TuBZs3LIQz6/giphy.gif', 'https://media.giphy.com/media/3GnKKEw2v7bXi/giphy.gif', 'https://media.giphy.com/media/GR1WWKadM9m0g/giphy.gif', 'https://media.giphy.com/media/iBpq5SbrYiSTTSHO7z/giphy.gif', 'https://media.giphy.com/media/dJirXKRo0j1l0j9V9Q/giphy.gif', 'https://media.giphy.com/media/ZvkFmclQO1ImmRNm0K/giphy.gif', 'https://media.giphy.com/media/82Mksc7tnX3qp4FVNN/giphy.gif', 'https://media.giphy.com/media/mTQhl6cWXDJBu/giphy.gif']
    embed=discord.Embed(title="Here's Your marvel GIF {}".format(ctx.message.author.name)", color=0Xf9fcfc)
    embed.set_footer(text=f'Requested by {ctx.message.author.name} ', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)
	

@client.command(pass_context = True)
async def dc(ctx):
    choices = ['https://media.giphy.com/media/uDPSXySAEDv56/giphy.gif', 'https://media.giphy.com/media/26vIg1DlkNdJr65q0/giphy.gif', 'https://media.giphy.com/media/jcIRoyJKQG3za/giphy.gif', 'https://media.giphy.com/media/26xBLVi4RuhYmV6zm/giphy.gif', 'https://media.giphy.com/media/xUOwGfcrlRjKjs2sSI/giphy.gif', 'https://media.giphy.com/media/l41Yq5KYEmbxFaeVq/giphy.gif', 'https://media.giphy.com/media/3o7abJW5ZuiByDelji/giphy.gif', 'https://media.giphy.com/media/xU67CtAMi8f5K/giphy.gif', 'https://media.giphy.com/media/VXQuKHDhTIBWM/giphy.gif']
    embed=discord.Embed(title="Here's Your dc GIF {}".format(ctx.message.author.name)", color=0Xf9fcfc)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532751889172004865/540387622418251780/100.gif')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context = True)
async def joker(ctx):
    choices = ['https://media.giphy.com/media/KZd26L2o8QXtK/giphy.gif', 'https://media.giphy.com/media/aazZrFTMrDKLK/giphy.gif', 'https://media.giphy.com/media/F0A48Q2wFjE7S/giphy.gif', 'https://media.giphy.com/media/7waKDy5RbDYVG/giphy.gif', 'https://media.giphy.com/media/13m24iFmhomZi0/giphy.gif', 'https://media.giphy.com/media/zCP1GdPjxtCTe/giphy.gif', 'https://media.giphy.com/media/tN2OR1R1BLKV2/giphy.gif', 'https://media.giphy.com/media/X9Z0O2bpi8GMU/giphy.gif', 'https://media.giphy.com/media/YPIrsRqqO7oB2/giphy.gif', 'https://media.giphy.com/media/FSp1Wqx2TPYSA/giphy.gif', 'https://media.giphy.com/media/8UwEdwAF5XWQE/giphy.gif']
    embed=discord.Embed(title="Here's Your joker GIF {}".format(ctx.message.author.name)",description="Tribute to the legendary **Heath Ledger**", color=0Xf9fcfc)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def rps(ctx, *, message=None):
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = 0xf9fcfc)
    embed.set_footer(text=f"playing by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    if message is None:
        await client.say('```The proper usage is \n!!rps <rock> or <paper> or <scissors>```')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)

		
@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0xf9fcfc)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0xf9fcfc)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
	
	
@client.command(pass_context=True, aliases=['members'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em =Embed(title="membercount")
    em.description =    "**\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "**" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)	 
	



@client.command(pass_context = True)
async def botinfo(ctx):
    embed = discord.Embed(title="Dab information", color=0Xf9fcfc)
    embed.add_field(name="__**Bot name**___", value="DAB", inline = True)
    embed.add_field(name="__**Bot id**__", value="520267296506249216", inline = True)
    embed.add_field(name="__**Bot prefix**__", value="!!", inline = True)
    embed.add_field(name="__**Bot language**__", value="Python", inline = True)
    embed.add_field(name="__**Creator**__", value="@marcos.#0290", inline = True)
    embed.add_field(name="__**Special Thanks To**__", value="@I'm Joker#7475")
    embed.add_field(name="__**Bot servers**__", value=str(len(client.servers)), inline = True)
    embed.add_field(name="__**Bot users**__", value=str(len(set(client.get_all_members()))), inline = True)
    embed.add_field(name="__**Invite bot**__", value="[click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot)", inline = True)
    embed.add_field(name="__**Support server**__", value="[click here](https://discord.gg/dFM9HG6)", inline = True)
    embed.add_field(name="If you have any queries about this BOT, DM me...", value="**@marcos.#0290**", inline = True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/532088532576239647/537947512347295774/100.gif')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)


	
@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(color=0Xf9fcfc)
    embed.set_author(name="Command prefix: !!")
    embed.add_field(name="__Administrator commands__", value="`serverinfo  :` server's information . \n`membercount  :` how many servers mamber in. \n`poll  :` Polling . \n`ban  :` ban the user. \n`clear  :` clear messages. \n`announce  :` To announce the entered **#channel** n **matter** . ", inline=True)
    embed.add_field(name="__Fun commands__", value="`virus  :` virus. \n`joke  :` tell you a joke ! . ")	
    embed.add_field(name="__Music commands__", value="`play  :` play the music you want. \n`pause  :` will pause the audio. \n`resume  :` will resume the audio. \n`skip  :` will skip the music. \n`stop  :` will Bot disconnected. \n`song  :` To Check The Current playing song. ") 
    embed.add_field(name="__Animals commands__", value="`fox  :` fox images. \n`dog  :` dog images. \n`cat  :` cat images. \n`bird  :` bird images. ")
    embed.add_field(name="__Games commands__", value="`rps  :` play the rock, paper and scissors.\n`rolldice  :` roll the dice and get 1 to 6 numbers. \n`flipcoin  :` flip the coin. ")
    embed.add_field(name="__Information commands__", value="`botinfo  :` Information about this BOT. \n`userinfo  :` user's information. \n`ping  :` pong.")
    embed.add_field(name="__Images commands__", value="`meme  :` meme image. \n`avatar  :` Avatar. \n`dc  :` DC GIF \n`marvel  :` Marvel GIF. \n`joker  :` Joker GIF. \n`slap  :` slap the user. \n`hug  :`  hug a user. \n`kiss  :` kiss the user. \n`lovedetect  :` lovedetect.  \n\n__support server__ - [click here](https://discord.gg/dFM9HG6) \n__bot invite__ - [click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot) \n\n__**more feautures coming soon...**__")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/537866862600650773/541121180921495554/maxresdefault.jpg') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)    	

	
client.run(os.getenv('Token')) 

