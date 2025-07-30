from typing import final

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import typing as T
from stat_calculation import stat_factory

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

@tree.command(name="convert_crit", description="Convert crit to %Final Crit.")
async def convert_crit(interaction,
                      amount: float):

    stat_clss = stat_factory('CRIT')
    out_msg = stat_clss.convert_input(input_type='raw', input_val=amount)
    await interaction.response.send_message(content=out_msg, ephemeral=True)

@tree.command(name="convert_aspd", description="Convert ASPD to %Final ASPD.")
async def convert_asdp(interaction,
                      amount: float):

    stat_clss = stat_factory('ASPD')
    out_msg = stat_clss.convert_input(input_type='raw', input_val=amount)
    await interaction.response.send_message(content=out_msg, ephemeral=True)

@tree.command(name="convert_haste", description="Convert Haste or %Final Haste to CD Reduction or CT Reduction.")
async def convert_haste(interaction,
                      amount: int,
                      stat:T.Literal['Haste', '%Final Haste'],
                      output: T.Literal['CT Reduction', 'CD Reduction']):

    input_type = 'raw' if stat == 'Haste' else 'final'
    stat_clss = stat_factory(output)
    out_msg = stat_clss.convert_input(input_type=input_type, input_val=amount)
    await interaction.response.send_message(content=out_msg, ephemeral=True)

@tree.command(name='how_much_more', description="Determine how much more stat you need to reach some target goal.")
async def how_much_more(interaction,
                          target_stat:T.Literal['ASPD', 'CRIT', 'CD Reduction', 'CT Reduction'],
                          target_amount:float,
                          stat_to_evaluate: T.Literal['raw', 'final'],
                          current_raw:int=0,
                          current_final:float=0.0):

    stat_clss = stat_factory(target_stat)
    out_msg = stat_clss.needed_input(current_raw=current_raw,
                                     current_final=current_final,
                                     stat_to_quant=stat_to_evaluate,
                                     target_amt=target_amount)

    await interaction.response.send_message(content=out_msg, ephemeral=True)


@tree.command(name='which_is_better', description="Compare Raw vs. %Final stat to see which is better.")
async def which_is_better(interaction,
                          target_stat: T.Literal['ASPD', 'CRIT', 'CD Reduction', 'CT Reduction'],
                          current_raw: int,
                          raw_added: int,
                          final_added: float,
                          current_final: float):

    stat_clss = stat_factory(target_stat)()
    out_msg = stat_clss.compare_inputs(raw=raw_added,
                                       final=final_added,
                                       current_raw=current_raw,
                                       current_final=current_final)


    await interaction.response.send_message(content=out_msg, ephemeral=True)


@bot.event
async def on_ready():
    # Sync commands on command tree with discord.
    await tree.sync()
    print(f"{bot.user} is now up and running.")


if __name__ == "__main__":
    bot.run(TOKEN)