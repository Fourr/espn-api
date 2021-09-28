import discord
import test2

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$scores'):
        await message.channel.send(test2.get_scores())

    if message.content.startswith('$projections'):
        await message.channel.send(test2.get_scores_projections())

client.run("token")
