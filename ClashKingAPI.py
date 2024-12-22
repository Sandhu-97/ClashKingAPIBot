import requests
from requirements import DATE

def get_player(tag:str):
    tag=tag.upper()
    tag=tag.replace("#", "")
    try:
        url = f"https://api.clashking.xyz/player/%23{tag}/stats"
        req = requests.get(url=url)
        data = req.json()
        return data
    except:
        print("ERROR: get_player: cannot fetch player")

def get_clan(tag:str):
    tag=tag.upper()
    tag=tag.replace("#", "")
    try:
        url = f"https://api.clashking.xyz/clan/%23{tag}/basic"
        req = requests.get(url=url)
        data = req.json()
        return data
    except:
        print("ERROR: get_clan: cannot fetch clan")
   

def get_player_stats(tag:str):
    player_json = get_player(tag)
    player_name = player_json['name']
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

    return [player_name, player_tag, attack_wins, donated+received]
