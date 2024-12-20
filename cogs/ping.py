import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    @commands.slash_command(description="Ping Latency")
    async def ping(self, inter:disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Pong: {round(self.bot.latency*1000)} ms")


def setup(bot:commands.InteractionBot):
    bot.add_cog(PingCommand(bot))