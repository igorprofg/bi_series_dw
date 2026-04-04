import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/discover/tv"

all_series = []

for page in range(1, 11):  # pega 10 páginas
    params = {
        "api_key": API_KEY,
        "with_genres": 80,  # crime
        "language": "en-US",
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = data.get("results", [])

    for serie in results:
        all_series.append(serie)

print(f"Total de séries coletadas: {len(all_series)}")

df = pd.DataFrame(all_series)

# salvar CSV bruto
df.to_csv("data/raw/series_raw.csv", index=False)