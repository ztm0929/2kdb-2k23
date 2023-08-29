import requests
import pandas as pd
import time  # 用于添加延迟

# 已正确编码的基础URL
base_url = 'https://2kdb.net/api/players/23/%7B%22page%22:%22{page}%22,%22version%22:%2223%22%7D'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
}

# 从指定的开始和结束页面获取所有数据
def fetch_all_data(start_page=1, end_page=165, delay_seconds=2):
    all_data = []
    for page_number in range(start_page, end_page + 1):  # 遍历每一页
        response = requests.get(base_url.format(page=page_number), headers=headers)  # 发起请求
        data = response.json()
        players_data = data['players']
        all_data.extend(players_data)  # 将数据添加到总列表中
        print(f"成功获取第{page_number}页的数据")  # 打印成功信息
        time.sleep(delay_seconds)  # 添加延迟
    df_players = pd.json_normalize(all_data)  # 将列表转换为DataFrame
    return df_players

# 将DataFrame导出为Excel文件
def export_to_excel(df, filename='players.xlsx'):
    df.to_excel(filename, index=False)

# 主执行部分
if __name__ == "__main__":
    data = fetch_all_data()  # 获取所有数据
    export_to_excel(data)  # 导出数据到Excel文件
