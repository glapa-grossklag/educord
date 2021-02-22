from discord.ext import commands
from discord.ext.commands import Context

import config

bot = commands.Bot(config.prefix)

@bot.event
async def on_ready():
    print("Ready as {}".format(bot.user))

@bot.command()
async def hello(ctx: Context):
    await ctx.reply("Hello, {}!".format(ctx.message.author))

bot.run(config.token)
