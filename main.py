import discord
import os
import requests
import json

client = discord.Client()

# makes request to API and parses returned JSON
# for a random quote with the author
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

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
  elif msg.content.startswith('$inspire'):
    quote = get_quote()
    await msg.channel.send(quote)

client.run(os.getenv('TOKEN'))
