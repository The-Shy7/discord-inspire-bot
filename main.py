import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = [
  "sad", 
  "depressed", 
  "unhappy", 
  "angry", 
  "somber", 
  "bitter", 
  "pessimistic", 
  "heartbroken", 
  "miserable", 
  "depressing"
  ]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are an amazing person!"
]

# makes request to API and parses returned JSON
# for a random quote with the author
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

# updates db when new encouraging messages are added to it
def update_encouragements(msg):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(msg)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [msg]

# updates db when encouraging messages are deleted
def delete_encouragements(index):
  encouragements = db["encouragements"]

  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


# called when bot is logged in and ready to be used 
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# called when bot receives a message
@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  msg_content = msg.content

  if msg_content.startswith('$hello'):
    # responds back with a "Hello!" after
    # detecting the command 
    await msg.channel.send('Hello!')
  elif msg_content.startswith('$inspire'):
    # responds back with an inspirational quote 
    # with its author after detecting the command 
    quote = get_quote()
    await msg.channel.send(quote)

  options = starter_encouragements

  if "encouragements" in db.keys():
    options = options + db["encouragements"]


  # if bot detects any "sad" word from the 
  # client's messages, then it will randomly respond with
  # an encouraging message from the list
  if any(word in msg_content for word in sad_words):
    await msg.channel.send(random.choice(options))

  # adds new encouraging messages to the db from clients
  # after the invoking "$new" command with their message 
  if msg_content.startswith('$new'):
    encouraging_msg = msg_content.split("$new ", 1)[1]
    update_encouragements(encouraging_msg)
    await msg.channel.send('New encouraging message added!')

  # deletes encouraging messages from the db
  # after the invoking "$del" command with an integer index 
  if msg_content.startswith('$del'):
    # if there's currently no encouragements in the db
    # return an empty list to client 
    encouragements = []

    # if there's currently encouragements in the db
    # return an updated list to client after deletion
    if "encouragements" in db.keys():
      index = int(msg_content.split("$del", 1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]

    await msg.channel.send(encouragements)

client.run(os.getenv('TOKEN'))
