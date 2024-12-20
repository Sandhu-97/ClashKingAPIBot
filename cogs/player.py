import disnake
from disnake.ext import commands
from requirements import DATE
from ClashKingAPI import get_player


class PlayerCommand(commands.Cog):

    def __init__(self, bot:commands.InteractionBot):
        self.bot = bot
    
    @commands.slash_command()
    async def player(self, inter:disnake.ApplicationCommandInteraction, tag: str):
        await inter.response.defer()
        player_json = get_player(tag)
        name = player_json['name']
        try:
            attack_wins = player_json['attack_wins'][DATE]
        except:
            attack_wins=0
        try:
            donated = player_json['donations'][DATE]['donated']
        except:
            donated=0
        try:
            received = player_json['donations'][DATE]['received'] 
        except:
            received=0
        embed = disnake.Embed(title=name, color=disnake.Color.green())
        embed.description=f"""Attack Wins: {attack_wins}
Donations: {donated+received}
"""
        await inter.followup.send(embed=embed)

def setup(bot:commands.InteractionBot):
    bot.add_cog(PlayerCommand(bot))