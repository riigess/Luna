from discord.ext import commands

from resources.DatabaseHandler import DatabaseHandler

class GenericCommands(commands.Cog):
	def __init__(self, dbh:DatabaseHandler, bot):
		self.dbh = dbh
		self.bot = bot

	@commands.command(pass_context=True)
	@commands.has_role("Mod")
	async def config(self, ctx, command_name:str, change:str):
		pass

	@commands.command(pass_context=True)
	async def amazon(self, ctx, url:str):
		self.dbh.
		if ctx.guild_id