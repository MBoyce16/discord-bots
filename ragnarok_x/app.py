from typing import final

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import typing as T
from stat_convert import formula_factory
from stat_convert.haste import CD_reduc, CT_reduc
from how_much_more.stat_calc import NeededStat

load_dotenv()

TOKEN = os.getenv("RAG_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name="help", description="Description of available commands.")
async def help(interaction):
    msg = f"TODO: provide summary of each function"
    await interaction.response.send_message(content=msg, ephemeral=True)

@tree.command(name="Raw to Final", description="Convert raw Crit, ASPD, or Haste to Final%.")
async def convert_raw(interaction, stat: T.Literal['Crit', 'Haste', 'ASPD'], amount:int):
    calc = formula_factory(stat)
    final_val = calc(amount)
    await interaction.response.send_message(content=f"Final {stat}: {final_val}%", ephemeral=True)

@tree.command(name="Convert Haste", description="Convert haste and/or final haste to CD and CT reduction.")
async def convert_haste(interaction, haste: int, final_haste: float):
    CD_calc = CD_reduc(haste, final_haste)
    CT_calc = CT_reduc(haste, final_haste)

    await interaction.response.send_message(content=f"CD Reduction: {CD_calc} secs\nCT Reduction: {CT_calc} secs", ephemeral=True)

@tree.command(name='How much more?', description="Determine how much more stat you need to reach some target goal.")
async def which_is_better(interaction,
                          target_stat:T.Literal['Crit', 'ASPD', 'CD Reduction', 'CT Reduction'],
                          target_amount:float,
                          stat_to_evaluate: T.Literal['raw', 'final'],
                          current_raw:int=0,
                          current_final:float=0):
    needed = NeededStat(stat=target_stat, needed_stat=stat_to_evaluate,
                        amount_stat_needed=target_amount,
                        current_raw = 0,
                        current_final=current_final)
    await interaction.response.send_message(content=f"Not implemented yet", ephemeral=True)

@tree.command(name='Which is better?', description="Compare Raw vs. %Final stat to see which is better.")
async def which_is_better(interaction, stat: T.Literal['Crit', 'Haste', 'ASPD'], amount:int):
    ...
    await interaction.response.send_message(content=f"Not implemented yet", ephemeral=True)

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