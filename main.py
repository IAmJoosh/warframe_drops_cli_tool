import requests
import json

def get_drops(endpoint, query):
    url = endpoint + query
    raw_drops = requests.get(url).json()
    drops = [relic for i,relic in enumerate(raw_drops, start=4) if i%4 == 0]
    return drops

endpoint = 'https://api.warframestat.us/drops/search/'
search_query = input("Enter drop: ")

with open('drops.json', 'w') as f:
    drops_json = json.dumps(get_drops(endpoint, search_query))
    f.writelines(drops_json)
    print(drops_json)