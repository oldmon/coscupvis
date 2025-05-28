def download_json(url, save_path):
    import requests
    import json

    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
    else:
        print(f"Failed to download data from {url}. Status code: {response.status_code}")

def load_json(file_path):
    import json

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_to_csv(data, file_path):
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')