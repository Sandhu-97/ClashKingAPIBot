import disnake
from disnake.ext import commands

from ClashKingAPI import get_clan, get_player
from requirements import CLAN_TAGS, DATE, CLAN_SHORTS
from database import insertIntoTable, clearTable

class LoadData(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.slash_command(name="loadplayers", description="Load Player Data into Database")
    async def loadplayers(self, inter:disnake.ApplicationCommandInteraction):
        await inter.response.defer()
        
        if (inter.author.id !=511918143791169536):
            await inter.followup.send('❌ Command is only available for bot owner', ephemeral=True)
            return;

        await inter.followup.send('Fetching data for all clans... _may take some time_')
        for tag in CLAN_TAGS:
            clan_json = get_clan(tag)
            clan_name = clan_json['name']
            clan_tag = clan_json['tag']
            clearTable(CLAN_SHORTS[tag])
            for member in clan_json['memberList']:
                try:
                    player_json = get_player(member['tag'])
                except:
                    print("cannot fetch", member, clan_name)
                player_name = player_json['name'] or "NULL"
                player_tag = player_json['tag']
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
                
                try:
                    insertIntoTable(CLAN_SHORTS[clan_tag], player_name, player_tag, attack_wins, donated+received)
                except:
                    print("unable to insert in db", player_name, player_tag)

        await inter.followup.send("All clans data loaded in database", ephemeral=True)


def setup(bot):
    bot.add_cog(LoadData(bot))