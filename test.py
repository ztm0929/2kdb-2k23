import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas  import json_normalize
import json

base_url = 'https://2kdb.net/api/players/23/%7B%22page%22:%22165%22,%22version%22:%2223%22%7D'
# 'https://2kdb.net/api/players/23/%7B%22page%22:%22{x}%22,%22version%22:%2223%22%7D'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
}

r = requests.get(base_url, headers=headers)

json_data = r.json()

output_file = 'players.json'
with open(output_file, 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

with open ('players.json', 'r') as f:
    data = json.load(f)

players_data = data['players']

df_players = json_normalize(players_data)
df = pd.DataFrame(players_data)

excel_file_name = 'player.xlsx'
df.to_excel(excel_file_name, index=False)



