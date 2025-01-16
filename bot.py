import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']

bot = commands.InteractionBot(test_guilds=[556053478812942366], owner_id=511918143791169536)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")

cogs = ['ping', 'reqr', 'loaddata', 'loadclan']

def load_cogs():
    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        # print(cog, 'loaded')
def unload_cogs():
    for cog in cogs:
        bot.unload_extension(f'cogs.{cog}')
        # print(cog, 'unloaded')

@bot.slash_command(description="Reload Cogs")
async def reload(inter:disnake.ApplicationCommandInteraction):
    if (inter.author.id !=511918143791169536):
        await inter.response.send_message('❌ Command is only available for bot owner', ephemeral=True)
        return
    unload_cogs()
    load_cogs()
    await inter.response.send_message("Cogs Reloaded", ephemeral=True)

@bot.slash_command(description="Load a Single Cog")
async def load(inter:disnake.ApplicationCommandInteraction, name:str):
    if (inter.author.id !=511918143791169536):
        await inter.response.send_message('❌ Command is only available for bot owner', ephemeral=True)
        return
    bot.load_extension(f"cogs.{name}")
    await inter.response.send_message("Cog Loaded", ephemeral=True)

@bot.slash_command(description="Unload a Single Cog")
async def unload(inter:disnake.ApplicationCommandInteraction, name:str):
    if (inter.author.id !=511918143791169536):
        await inter.response.send_message('❌ Command is only available for bot owner', ephemeral=True)
        return
    bot.unload_extension(f"cogs.{name}")
    await inter.response.send_message("Cog Unloaded", ephemeral=True)

load_cogs()
bot.run(BOT_TOKEN)