# grabs prem results for the last few seasons from football-data.co.uk
import os
import requests
import pandas as pd

SEASONS = ["2324", "2425", "2526", "2627"]
URL = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"

os.makedirs("data", exist_ok=True)

for season in SEASONS:
    r = requests.get(URL.format(season=season), timeout=30)
    r.raise_for_status()
    path = f"data/E0_{season}.csv"
    with open(path, "wb") as f:
        f.write(r.content)
    print("saved", path)

df = pd.read_csv("data/E0_2627.csv")
print(df[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "Referee"]].tail(10))