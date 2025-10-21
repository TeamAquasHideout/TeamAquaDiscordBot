import discord
from discord.ext import commands

command_reponses = {
    "!pret" : "https://discord.gg/d5dubZ3",
    "!RHH" : "https://discord.com/invite/6CzjAG6GZk",
    "!3ds" : "https://discord.gg/G8ZrcUWKcS",
    "!ds" : "https://discord.com/invite/zAtqJDW2jC \n https://discord.gg/YBtdN3aXfv",
    "!tutorials" : "[Video Tutorials](<https://www.youtube.com/playlist?list=PLLNv9Lq6kDmTIYfN5NvgQRvfOHTOXl0uU>)\n\
[pokeemerald Wiki Tutorials](<https://github.com/pret/pokeemerald/wiki/Tutorials>)\n\
[The Basics Of Scripting](<https://github.com/pret/pokeemerald/wiki/The-Basics-of-Scripting>)\n\
[The Basics of Github](<https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo/wiki/The-Basics-of-GitHub>)",
    "!taar" : "[Team Aqua Asset Repo](<https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo>)",
	"!decomp" : "## Decomp Resources:\n\
[Pokemon Emerald Decomp Source Code](<https://github.com/pret/pokeemerald>)\n\
[Porymap Download](<https://github.com/huderlem/porymap>)\n\
[Porymap Documentation](<https://huderlem.github.io/porymap/manual/introduction.html>)\n\
[Poryscript Download](<https://github.com/huderlem/poryscript>)\n\
[pokeemerald-expansion Decomp Hack Base](<https://github.com/rh-hideout/pokeemerald-expansion>)\n\
[Pokemon FireRed Decomp Source Code](<https://github.com/pret/pokefirered>)",
	"!tonc" : "[TONC - GBA Programming Guide](<https://www.coranac.com/tonc/text/toc.htm>)",
	"!expansion" : "[The pokeemerald-expansion Source Code](<https://github.com/rh-hideout/pokeemerald-expansion>)\n\
[RHH Discord - Home of Expansion Development](https://discord.com/invite/6CzjAG6GZk)",
	"!hma" : "Get out of here ya filthy b*nary hacker, you belong here: \nhttps://discord.com/invite/x9eQuBg",
	"!ghguide" : "[Team Aqua Github Tutorial](<https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo/wiki/The-Basics-of-GitHub>)",
}


class AquaCommands(commands.Cog, name="Team Aqua Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help="Join the Team Aqua Grunts", category="Team Aqua Commands")
	async def grunt(self, ctx):
		# Get the role object
		role = discord.utils.get(ctx.guild.roles, name='Team Aqua Grunt')
		if role is None:
			await ctx.send(f"Role '{'Team Aqua Grunt'}' not found!")
			return

		# Assign the role to the command invoker
		await ctx.author.add_roles(role)
		await ctx.send(f"{ctx.author.mention} pledged allegiance to Team Aqua!")


	@commands.command(help="Link: RHH server", category="Team Aqua Commands")
	async def rhh(self, ctx):
		await ctx.send(command_reponses["!RHH"])	
		
	@commands.command(help="Link: pret server", category="Team Aqua Commands")
	async def pret(self, ctx):
		await ctx.send(command_reponses["!pret"])	

	@commands.command(help="Link: DS Romhack Server", category="Team Aqua Commands")
	async def ds(self, ctx):
		await ctx.send(command_reponses["!ds"])	

	@commands.command(help="Link: 3DS Romhack Server", category="Team Aqua Commands")
	async def hack3ds(self, ctx):
		await ctx.send(command_reponses["!3ds"])	

	@commands.command(help="Link: Text / Video Tutorials", category="Team Aqua Commands")
	async def tutorials(self, ctx):
		await ctx.send(command_reponses["!tutorials"])	

	@commands.command(help="Link: Team Aqua Asset Repo", category="Team Aqua Commands")
	async def taar(self, ctx):
		await ctx.send(command_reponses["!taar"])	

	@commands.command(help="Link: Github Tutorial/Guide", category="Team Aqua Commands")
	async def ghguide(self, ctx):
		await ctx.send(command_reponses["!ghguide"])	
	
	@commands.command(help="Link: Decomp and Resources", category="Team Aqua Commands")
	async def decomp(self, ctx):
		await ctx.send(command_reponses["!decomp"])
	
	@commands.command(help="Link: TONC Programming Guide", category="Team Aqua Commands")
	async def tonc(self, ctx):
		await ctx.send(command_reponses["!tonc"])
	
	@commands.command(help="Link: pokeemerald-expansion", category="Team Aqua Commands")
	async def expansion(self, ctx):
		await ctx.send(command_reponses["!expansion"])
	
	@commands.command(help="Link: B*nary Hackers Go Here", category="Team Aqua Commands")
	async def hma(self, ctx):
		await ctx.send(command_reponses["!hma"])

async def setup(bot):
    await bot.add_cog(AquaCommands(bot))
