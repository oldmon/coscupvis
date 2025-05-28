import requests
import os

def download_json(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Downloaded data from {url} to {save_path}")
    else:
        print(f"Failed to download data from {url}. Status code: {response.status_code}")

def main():
    base_url = "https://coscup.org/{year}/json/session.json"
    years = [2020, 2021, 2022, 2023, 2024]
    raw_data_dir = os.path.join(os.path.dirname(__file__), '../data/raw/sessions')

    os.makedirs(raw_data_dir, exist_ok=True)

    for year in years:
        url = base_url.format(year=year)
        save_path = os.path.join(raw_data_dir, f"{year}.json")
        download_json(url, save_path)

if __name__ == "__main__":
    main()