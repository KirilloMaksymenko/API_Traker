import requests
import json
import config

def request_contr_strike_api(user_id):
    request_url = f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={config.steam_api_key}&steamid={user_id}"
    rqst = requests.get(request_url)
    print(rqst)

    if rqst == "<Response [500]>":
        return "Account is not public"

    csgo_stats = rqst.json()
    for stat in csgo_stats["playerstats"]["stats"]:
        if stat["name"] == "total_kills":
            kills = stat["value"]

    for stat in csgo_stats["playerstats"]["stats"]:
        if stat["name"] == "total_deaths":         
            kd = kills / stat["value"]

    for stat in csgo_stats["playerstats"]["stats"]:
        if stat["name"] == "total_matches_played":         
            matches = stat["value"]

    for stat in csgo_stats["playerstats"]["stats"]:
        if stat["name"] == "total_mvps":         
            mvp = stat["value"]

    content = {
        "matches":matches,
        "mvp":mvp,
        "kills":kills,
        "kd":kd,
    }

    return content

