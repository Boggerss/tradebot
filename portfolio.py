import SandPwebscraper as stocks

startSum = "{:.2f}".format(100000.00)
shares = 0

async def Symbol(ctx, companySymbol: str):
    values = stocks.symbol_input(companySymbol) # stocks function will return values and store it in 'values' variable

    await ctx.send(values) # send values