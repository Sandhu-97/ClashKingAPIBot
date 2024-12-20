import requests
from datetime import datetime
from requirements import JC_ATTACK_WINS, JC_DONATIONS

def get_player(tag:str):
    tag=tag.upper()
    tag=tag.replace("#", "")
    url = f"https://api.clashking.xyz/player/%23{tag}/stats"
    req = requests.get(url=url)
    data = req.json()
    return data

def get_clan(tag:str):
    tag=tag.upper()
    tag=tag.replace("#", "")
    url = f"https://api.clashking.xyz/clan/%23{tag}/basic"
    req = requests.get(url=url)
    data = req.json()
    return data


month = datetime.now().month
year = datetime.now().year
year_month_string = f"{year}-{month}"


# data=get_player("#y8cpqg8pg")

# clan = get_clan("9JUVCV0L")
# for member in clan['memberList']:
#     player = get_player(member['tag'])
#     attack_wins=player['attack_wins'][year_month_string]
#     donations = player['donations'][year_month_string]['donated']+player['donations'][year_month_string]['received']
#     if (attack_wins<JC_ATTACK_WINS):
#         print("Attack Wins:", player['name'], attack_wins)
#     if (donations<JC_DONATIONS):
#         print("Donations: ", player['name'], donations)
    
# print(data['name'])
# data=get_player("2PP")
# print(data['name'])

# print(data['donations'][year_month_string]['donated']+data['donations'][year_month_string]['received'])
# print(data['attack_wins'][year_month_string])
