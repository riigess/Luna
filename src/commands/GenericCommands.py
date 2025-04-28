from discord.ext import commands

from resources.DatabaseHandler import DatabaseHandler

class GenericCommands(commands.Cog):
    def __init__(self, dbh:DatabaseHandler, bot):
        self.dbh = dbh
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role("Mod")
    async def config(self, ctx, command_name:str, change_to:str):
       pass

    @commands.command(pass_context=True)
    async def amazon(self, ctx, url:str):
        ref_endian = self.dbh.get_command_alias_response(ctx.guild.id, 'amazon')
        if len(ref_endian) == 0:
            return
        if ref_endian[0] == '/':
            ref_endian = ref_endian[1:]
        has_embed = '<' not in url and '>' not in url
        if not has_embed:
            url = url[1:-1]
        if '<' == url[0]:
            url = url[1:]
        if '>' == url[-1]:
            url = url[:-1]
        if "amazon.com" in url:
            await ctx.message.reply(f"Not required, but this would be helpful to support the community!\n{url}/{ref_endian}")
        if has_embed:
            await ctx.message.edit(suppress=True)
