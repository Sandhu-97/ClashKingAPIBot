import requests

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