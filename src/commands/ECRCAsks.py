from discord.ext import commands
import discord
from test.mock_socket import reply_with

class ECRC(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def amazon(self, ctx, url:str):
        has_embed = '<' not in url and '>' not in url
        if '<' == url[0]:
            url = url[1:]
        if '>' == url[-1]:
            url = url[:-1]
        if "https://amazon.com" in url or "https://www.amazon.com" in url:
            await ctx.message.reply(f"Not required, but this would be helpful to support ECRC! \n{url}/?&linkCode=sl2&tag=ecrc-20")
        else:
            await ctx.message.reply(f"ERR: amazon.com not found. Found {url} instead.")
        print("SCAMAZON LINK DEETS:", url, has_embed)
        if has_embed:
            await ctx.message.edit(suppress=True)
