import discord
from discord.ext import commands
# from discord.ext.commands import bot
import responses
import os
import requests
import random
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

async def send_message(message, user_message, is_private):
  try:
    response = responses.get_response(user_message)
    await message.reply(
      response, mention_author=True) if is_private else await message.reply(
        response)  # Use reply not sent to reply and mention the user

  except Exception as e:
    print(e)

#Random picture from file pics
def get_random_file():
  files =os.listdir('pics/')
  return random.choice(files)



def run_discord_bot():
  # TOKEN = ''
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
  #First Command
  bot = commands.Bot(command_prefix='/',
                    intents=intents)  
  #Next line is For the image
  
  @client.event
  async def on_ready():
    print(f'{client.user} is now runing!')
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.lower() == "help": #lower() for lowercasing
      embed = discord.Embed(title="My Meows",
                            description="Commands list, actually they're not really commands, yet!",
                            color=0xb0b0ff)
      embed.add_field(name="help",
                      value="```TRY :hi , bye\t  \
                            \n\t hello cat\t \n\t love you\t\
                            \n\t roll\t  \n\t owner\t \n\t cat pic\
                            \n\t and more coming ! ```:wink:",
                      inline=True) #this is actually a good embed 
      await message.channel.send(embed=embed)
      
    if message.content.lower()=='meow':
      if message.author.name == ".baselabouelnour":
        await message.channel.send(f"`MEOW` {message.author.mention}`!`")
      elif message.author.name == "Segma_3":
        await message.channel.send(f"`Special Moew!`:kissing_cat:")
      elif message.author.name == "Crombo":
        await message.channel.send("`no`")
        await message.add_reaction('👍')
      else:
        await message.channel.send(f"`normal meow` {message.author.mention}`!`")
    
    #BREAKING NEWS!!!IT IS ALMOST WORKING
    if message.content.lower()=='cat pic':
        file = get_random_file()
        with open("pics/"+file,"rb") as f:
          picture = discord.File(f)
          embed = discord.Embed(title="meow!",
                                description="Random Cat Pic",
                                color=0xb0b0ff)  #for better format
          embed.set_image(url="attachment://"+file)
          # await message.channel.send(file = picture) 
          await message.reply(file=picture, embed=embed) #same as last line but just better format
    
    #Recation when name said , no raction for mention right now
    if message.content.lower()=='firstcat':
        await message.add_reaction('👍')

    #Display User information on terminal
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username} said : "{user_message}" ({channel})')

    #Messages
    if user_message[0] == '?':
      user_message = user_message[1:]
      await send_message(message, user_message, is_private=True)
    else:
      await send_message(message, user_message, is_private=False)

  keep_alive()
  client.run(my_secret)
