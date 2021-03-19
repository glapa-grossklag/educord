from discord.ext import commands
from discord.ext.commands import Context
from notebook import Notebook, Note

import config
import json
import discord


def write_json(data, filename=config.datafile):
    with open(filename, 'w') as f:
        json.dump(data, f)


bot = commands.Bot(config.prefix)


@bot.command()
async def createNotebook(ctx, name: str):
    data = {}
    try:
        with open(config.datafile, 'r') as f:
            data = json.load(f)
    except IOError:
        with open(config.datafile, 'w') as f:
            # Initialize the datafile with an empty dict
            json.dump(data, f)


    if name in data:
        ctx.reply("A notebook with that name already exists")
    else:
        new = Notebook(name)
        data.append(new)
        write_json(data)


@bot.command()
async def addNote(ctx, notebook: Notebook, name: str, value: str):
    with open(config.datafile, 'r') as f:
        data = json.load(f)
    if notebook in data:
        if name not in data:
            data[notebook][name] = value
            write_json(data)
        else:
            ctx.reply("This note already exists in this notebook")
    else:
        ctx.reply("This notebook does not exist")


@bot.command()
async def deleteNote(ctx, notebook: str, note: str):
    with open(config.datafile, 'r') as f:
        data = json.load(f)
    if notebook in data:
        if note in data[notebook]:
            data[notebook].pop(note)
            ctx.reply("Deleted `{}` from `{}`".format(note, notebook))
        else:
            ctx.reply("Invalid note: {}".format(note))
    else:
        ctx.reply("Invalid notebook: {}".format(notebook))


@bot.command(pass_context=True, name="notebook")
async def displayNotebook(ctx, notebook: str):
    channel = ctx.message.channel

    with open(config.datafile, 'r') as f:
        data = json.load(f)

    if notebook in data:
        embed = discord.Embed(
            title=data[notebook]
            # color=discord.Color.yellow()
        )
        for note in data[notebook]:
            embed.add_field(name=note, value=data[notebook][note], inline=True)

        await ctx.send_message(channel, embed=embed)
    else:
        await ctx.reply("Invalid notebook: {}".format(notebook))


@bot.event
async def on_ready():
    print("Ready as {}".format(bot.user))


@bot.command()
async def hello(ctx: Context):
    await ctx.reply("Hello, {}!".format(ctx.message.author))

bot.run(config.token)
