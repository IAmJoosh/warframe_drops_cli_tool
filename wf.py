import requests
import argparse

WFAPI_DROPS_ENDPOINT = 'https://api.warframestat.us/drops/search/'
EXCLUSIONS = ['Exceptional', 'Flawless', 'Radiant']
MEME = "Bronco Prime Blueprint"

def get_drops(query):
    url = WFAPI_DROPS_ENDPOINT + query
    drops = requests.get(url).json()
    return drops

def print_filtered_results(results):
    for drop in results:
        if EXCLUSIONS[0] not in drop['place'] and EXCLUSIONS[1] not in drop['place'] and EXCLUSIONS[2] not in drop['place']:
            print(f"Place: {drop['place']}\nItem: {drop['item']}\nRarity: {drop['rarity']}\nChance: {drop['chance']}%\n")

parser = argparse.ArgumentParser(description="Warframe CLI helper tool to find drop locations for items.")
parser.add_argument('query', nargs='+', default=MEME, help="The item for which you would like to seach.")
args = parser.parse_args()

query = " ".join(args.query)

results = get_drops(query)
print_filtered_results(results)