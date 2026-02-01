import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

df = pd.DataFrame({
    "x": range(100),
    "y": [i * 2 for i in range(100)]
})

df.to_csv("data/raw/data.csv", index=False)
print("Data downloaded")


