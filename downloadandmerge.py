import requests
import json
import os

years = [2020, 2021, 2022, 2023, 2024]
base_url = "https://coscup.org/{}/json/session.json"
all_sessions = []

os.makedirs("raw", exist_ok=True)

for year in years:
    url = base_url.format(year)
    print(f"Downloading {url} ...")
    resp = requests.get(url)
    data = resp.json()
    # 存原始檔
    with open(f"raw/session_{year}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # 加入年度欄位並合併
    for session in data.values():
        session['year'] = year
        all_sessions.append(session)

# 合併後存成一個 JSON 檔
with open("all_sessions_2020_2024.json", "w", encoding="utf-8") as f:
    json.dump(all_sessions, f, ensure_ascii=False, indent=2)

print("All sessions downloaded and merged!")