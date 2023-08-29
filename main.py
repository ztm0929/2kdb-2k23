import requests
from bs4 import BeautifulSoup

base_url = 'https://2kdb.net/players/23'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
}

def fetch_data_frome_url(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        player_name = soup.select_one('span', class_='font-bold').get_text()

        return player_name
    else:
        print(f"数据获取失败。错误码：{response.status_code}")
        return None
    
data = fetch_data_frome_url(base_url)
print(data)