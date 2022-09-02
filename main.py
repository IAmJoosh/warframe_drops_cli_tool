import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('drop', nargs = '+', help = "The item for which you want to find relic drop data")
args = parser.parse_args()

def get_drops(endpoint, query):
    url = endpoint + query
    raw_drops = requests.get(url).json()
    drops = [relic for i,relic in enumerate(raw_drops, start=4) if i%4 == 0]
    return drops

endpoint = 'https://api.warframestat.us/drops/search/'
# drop = input("Enter drop: ")
drop = '%20'.join(args.drop)

with open('drops.json', 'w') as f:
    drops_json = json.dumps(get_drops(endpoint, drop))
    f.writelines(drops_json)
    print(drops_json)