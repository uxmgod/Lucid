 # [Config]
prefix = "~" # The desired token to be used for the bot
token = "" # Instructions on how to get this in README.md

# [Main]
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix=prefix, self_bot=True)

print("Attempting to loggin to Discord account...\n")

@client.event
async def on_ready():
    print ("Lucid successfully logged into Discord\n")
    print ("Name: {}#{}".format(client.user.name, client.user.discriminator))
    print ("ID: {}\n".format(client.user.id))
    print ("Commands: Clear, Info")

@client.command(pass_context=True)
async def clear(ctx, limit: int=None):
    async for msg in client.logs_from(ctx.message.channel, limit=limit):
        if client.user.id == msg.author.id:
            try:
                await client.delete_message (msg)
            except:
                pass
    em = discord.Embed(title='Lucid', description="Messages purged :crystal_ball:", color=0x00FFFF)
    await client.say (embed=em)

async def info(ctx, limit: int=None):
    if client.user.id == msg.author.id:
        em = discord.Embed(title='Lucid', description="Created by Ninja#9525 @ https://github.com/neenjapolygon", color=0x00FFFF)
        client.say(embed=em)

client.run(token, bot=False)
