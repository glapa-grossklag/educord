from discord.ext import commands
from discord.ext.commands import Context

import config
import notebook
import json
import discord

bot = commands.Bot(config.prefix)


@bot.command()
async def createNotebook(ctx, name):
    name = Notebook(name)


@bot.command(pass_context=True, name="notebook")
async def displayNotebook(ctx, name):
    channel = ctx.message.channel

    with open("data.json") as f:
        data = json.load(f)

    if name in data:
        notebook = discord.Embed(
            title=data[name]
            # color=discord.Color.yellow()
        )
        for note in data[name]:
            notebook.add_field(name=note, value=data[name][note], inline=True)

        await ctx.send_message(channel, embed=notebook)

    else:
        await ctx.send_message(channel, "{}, this notebook does not exist".format(ctx.message.author))


@bot.event
async def on_ready():
    print("Ready as {}".format(bot.user))


@bot.command()
async def hello(ctx: Context):
    await ctx.reply("Hello, {}!".format(ctx.message.author))

bot.run(config.token)
