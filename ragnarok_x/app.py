import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import typing as T

load_dotenv()

TOKEN = os.getenv("TOKEN")



intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name="help", description="A basic help command.")
async def help(interaction):
    #  Since now we have interaction we can send the message as an ephemeral message.
    #  We also dont have to deal with deleting the command message.
    await interaction.response.send_message(content="Help command.", ephemeral=True)

@tree.command(name="raw-to-final", description="Convert raw Crit, ASPD, or Haste to Final%.")
async def convert_haste(interaction, stat: T.Literal['crit', 'haste', 'aspd'], amount:int):
    calc = formula_factory(stat)
    if calc is None:
        await interaction.response.send_message(content=f"{stat} not correct. Use haste, crit, or aspd.", ephemeral=True)

    fval = calc(amount)
    await interaction.response.send_message(content=f"Final Crit: {fval}%", ephemeral=True)

@tree.command(name="haste-convert", description="Convert haste and final haste to CD and Cast reduction.")
async def convert_haste(interaction, haste: int, final_haste: float):


    await interaction.response.send_message(content=f"Final Crit: {fval}%", ephemeral=True)

async


@bot.event
async def on_ready():
    # Sync commands on command tree with discord.
    await tree.sync()
    print(f"{bot.user} is now up and running.")


# @bot.command()
# async def convert_crit(ctx, crit: int):
#     fcrit = crit_to_final_crit(crit)
#     await ctx.send(f"Final Crit: {fcrit}%")
#
# @bot.command()
# async def convert_aspd(ctx, aspd: int):
#     faspd = aspd_to_final_aspd(aspd)
#     await ctx.send(f"Final ASDP: {faspd}%")
#
# @bot.command()
# async def convert_haste(ctx, haste: int):
#     fhaste = haste_to_final_haste(haste)
#     await ctx.send(f"Final Haste: {fhaste}%")



if __name__ == "__main__":
    bot.run(TOKEN)