import disnake
from disnake.ext import commands
from database import getMinAttacksData, getMinDonationsData, getLink
from requirements import CLAN_SHORTS, CLAN_TAGS, CLAN_REQUIREMENTS, CLAN_NAMES

class Reqr(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.slash_command()
    async def reqr(self, inter:disnake.ApplicationCommandInteraction, clan = commands.Param(choices=[
        disnake.OptionChoice("JOHN CENA", CLAN_TAGS[0]),
        disnake.OptionChoice("#1 Elite", CLAN_TAGS[1]),
        disnake.OptionChoice("playyboys♥", CLAN_TAGS[2]),
        disnake.OptionChoice("HELL BOYS", CLAN_TAGS[3]),
        disnake.OptionChoice("AvengerS.", CLAN_TAGS[4]),
        disnake.OptionChoice("ELITE GAMERZ", CLAN_TAGS[5]),
        disnake.OptionChoice("sports game", CLAN_TAGS[6]),
    ])):
        await inter.response.defer()
        
        attacks_data = getMinAttacksData(CLAN_SHORTS[clan], CLAN_REQUIREMENTS[clan][0])
        donations_data = getMinDonationsData(CLAN_SHORTS[clan], CLAN_REQUIREMENTS[clan][1])

        embed = disnake.Embed(title=f"**{CLAN_NAMES[clan]} Members Below Season Requirements**", color=disnake.Color.red())
        attacks="__**Attacks**__"
        for row in attacks_data:
            userid = getLink(row[1])
            if (userid is None):
                userid=0
            else:
                userid=userid[0]
            attacks = f"{attacks}\n {row[0]} *{row[1]}* - **{str(row[2])}** attacks - <@{userid}>"
        donations = "__**Donations**__"
        for row in donations_data:
            userid = getLink(row[1])
            if (userid is None):
                userid=0
            else:
                userid=userid[0]
            donations = f"{donations}\n {row[0]} *{row[1]}* - **{str(row[2])}** donations - <@{userid}>"

        embed.description=attacks+"\n\n"+donations
        await inter.followup.send(embed=embed)

def setup(bot):
    bot.add_cog(Reqr(bot))
