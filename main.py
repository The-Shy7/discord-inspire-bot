import discord

client = discord.Client()

# called when bot is ready to be used 
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# called when bot receives a message
@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('$hello'):
    await msg.channel.send('Hello!') 