import pandas as pd

df = pd.read_csv("devices.csv")

duplicates = df[df.duplicated("id", keep=False)]
print(duplicates)