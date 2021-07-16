import discord

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("$hello"):
		await message.channel.send('Hello!')
#unsafe need to store it secretly and then regenerate 
client.run("Tx7BSTdxSM5zYGb0mt8ghFCCQPOJS8Vl")