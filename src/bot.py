from discord.ext import commands
from discord.ext.commands import Context
from notebook import Notebook, Note

import config
import json
import discord

bot = commands.Bot(config.prefix)


def write_json(data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)


@bot.command()
async def createNotebook(ctx, name: str):
    with open("data.json", 'r') as f:
        data = json.load(f)

    if name in data:
        ctx.reply("A notebook with that name already exists")
    else:
        new = Notebook(name)
        data.append(new)
        write_json(data)


@bot.command()
async def deleteNote(ctx, notebook: str, note: str):
    with open("data.json", 'r') as f:
        data = json.load(f)
    if notebook in data:
        if note in data[notebook]:
            data[notebook].pop(note)
            ctx.reply("Successfully deleted note")
        else:
            ctx.reply("{}, sorry this note does not exist".format(
                ctx.message.author))
    else:
        ctx.reply("%s, sorry this notebook does not exist" %
                  ctx.message.author)


@bot.command(pass_context=True, name="notebook")
async def displayNotebook(ctx, name):
    channel = ctx.message.channel

    with open("data.json", 'r') as f:
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
