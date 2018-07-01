import discord

client = discord.Client()

@client.event
async def on_message(message):
    # this project/bot is made by fruskei
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!loveme'):
        await client.send_message(message.channel, "i love u sweetie")
    elif message.content.startswith('!kys'):
        await client.send_message(message.channel, "no u")
    elif message.content.startswith('!killme'):
        await client.send_message(message.channel, "the death note killed ya, im innocent i tell ya")



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDYyMjY4NDc0MjQ1MjUxMDcy.DhhmjQ.0_RMTpDIv_OPhQZJNg14WizefRk')
