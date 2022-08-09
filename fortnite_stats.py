import requests
import json
import config

def request_fortnite_api(username):
    request_url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"

    return json.loads(requests.get(request_url,headers={'Authorization':config.fortnite_api_key},params={'distplayName':username}).content)

def sort_data_fortnite(username):
    data = request_fortnite_api(username)

    name = data["data"]["account"]["name"]
    bp_lvl = data["data"]["battlePass"]["level"]
    matches = data["data"]["stats"]["all"]["overall"]["matches"]
    wins = data["data"]["stats"]["all"]["overall"]["wins"]
    kills = data["data"]["stats"]["all"]["overall"]["kills"]
    kd = data["data"]["stats"]["all"]["overall"]["kd"]
    content_all = {
        "name":name,
        "bp_lvl":bp_lvl,
        "matches":matches,
        "wins":wins,
        "kills":kills,
        "kd":kd,

    }
    
    matches_solo = data["data"]["stats"]["all"]["solo"]["matches"]
    wins_solo = data["data"]["stats"]["all"]["solo"]["wins"]
    kills_solo = data["data"]["stats"]["all"]["solo"]["kills"]
    kd_solo = data["data"]["stats"]["all"]["solo"]["kd"]
    content_solo = {
        "matches":matches_solo,
        "wins":wins_solo,
        "kills":kills_solo,
        "kd":kd_solo,

    }

    matches_duo = data["data"]["stats"]["all"]["duo"]["matches"]
    wins_duo = data["data"]["stats"]["all"]["duo"]["wins"]
    kills_duo = data["data"]["stats"]["all"]["duo"]["kills"]
    kd_duo = data["data"]["stats"]["all"]["duo"]["kd"]
    content_duo = {
        "matches":matches_duo,
        "wins":wins_duo,
        "kills":kills_duo,
        "kd":kd_duo,

    }

    matches_squad = data["data"]["stats"]["all"]["squad"]["matches"]
    wins_squad = data["data"]["stats"]["all"]["squad"]["wins"]
    kills_squad = data["data"]["stats"]["all"]["squad"]["kills"]
    kd_squad = data["data"]["stats"]["all"]["squad"]["kd"]
    content_squad = {
        "matches":matches_squad,
        "wins":wins_squad,
        "kills":kills_squad,
        "kd":kd_squad,

    }

    return content_all, content_solo, content_duo, content_squad


