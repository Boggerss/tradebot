# bot.py
import os
import SandPwebscraper as stocks
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'symbol', help = 'Type in all-caps symbol of company (ex. when searching for Apple, type AAPL).')
async def Symbol(ctx, companySymbol: str):
    values = stocks.symbol_input(companySymbol) # stocks function will return values and store it in 'values' variable

    await ctx.send(values) # send values

@bot.command()
async def viewall(ctx):
    contents = [stocks.viewallSect1(), 
                stocks.viewallSect2(), 
                stocks.viewallSect3(), 
                stocks.viewallSect4(),
                stocks.viewallSect5(), 
                stocks.viewallSect6(), 
                stocks.viewallSect7(), 
                stocks.viewallSect8(),
                stocks.viewallSect9(), 
                stocks.viewallSect10(), 
                stocks.viewallSect11(), 
                stocks.viewallSect12(),
                stocks.viewallSect13(), 
                stocks.viewallSect14(), 
                stocks.viewallSect15(), 
                stocks.viewallSect16(),
                stocks.viewallSect17(), 
                stocks.viewallSect18(), 
                stocks.viewallSect19(),
                stocks.viewallSect20(), 
                stocks.viewallSect21(), 
                stocks.viewallSect22(), 
                stocks.viewallSect23(),
                stocks.viewallSect24(), 
                stocks.viewallSect25(), 
                stocks.viewallSect26()]
    pages = 26
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds

bot.run(TOKEN)