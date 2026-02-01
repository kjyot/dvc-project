import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/data.csv")

df["z"] = df["x"] + df["y"]

df.to_csv("data/processed/data.csv", index=False)

print("Preprocessing done")

