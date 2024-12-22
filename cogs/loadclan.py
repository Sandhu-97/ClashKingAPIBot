import disnake
from disnake.ext import commands
from requirements import CLAN_TAGS, DATE, CLAN_SHORTS
from ClashKingAPI import get_clan, get_player_stats
from database import insertIntoTable, clearTable

class LoadClan(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.slash_command(description="Load a Single Clan Players")
    async def loadclan(self, inter:disnake.ApplicationCommandInteraction, clan = commands.Param(choices=[
        disnake.OptionChoice("JOHN CENA", CLAN_TAGS[0]),
        disnake.OptionChoice("#1 Elite", CLAN_TAGS[1]),
        disnake.OptionChoice("playyboys♥", CLAN_TAGS[2]),
        disnake.OptionChoice("HELL BOYS", CLAN_TAGS[3]),
        disnake.OptionChoice("AvengerS.", CLAN_TAGS[4]),
        disnake.OptionChoice("ELITE GAMERZ", CLAN_TAGS[5]),
        disnake.OptionChoice("sports game", CLAN_TAGS[6]),
    ])):
        await inter.response.defer()
        if (inter.author.id !=511918143791169536):
            await inter.followup.send('❌ Command is only available for bot owner', ephemeral=True)
            return;

        clan_json = get_clan(clan)
        clan_name = clan_json['name']
        clan_tag = clan_json['tag']
        await inter.followup.send(f'Fetching data for {clan_name}... *may take some time*')
        clearTable(CLAN_SHORTS[clan_tag])
        for member in clan_json['memberList']:
            player_stats = get_player_stats(member['tag'])
            
            try:
                insertIntoTable(CLAN_SHORTS[clan_tag], player_stats[0],player_stats[1], player_stats[2], player_stats[3])
            except:
                print("unable to insert in db", player_stats[0],player_stats[1])
        
        await inter.followup.send(f'Data for {clan_name} loaded successfully')


def setup(bot):
    bot.add_cog(LoadClan(bot))