import random
from discord import Game
from discord.ext.commands import Bot
worker: python3 bot.py

TOKEN = "NDYyMjY4NDc0MjQ1MjUxMDcy.DhjYcQ.ofg0Y5OzCzQWFNwFk9-S1JN6wpo"

BOT_PREFIX = "/"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball'
                ,description='answers gay yes/no questions'
                ,brief='basically like a real 8ball'
                ,pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'no',
        'maybe',
        'no u',
        'maybe not',
        'yes',
        'might be',
        'idk'
    ]
    await client.say(random.choice(possible_responses) +  ', ' + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + ' squared is ' + str(squared_value))

@client.event
async def on_ready():
    await client.change.presence(game=Game(name="being a good anime waifu"))
    print('logged in as ' + client.user.name)


client.run(TOKEN)
