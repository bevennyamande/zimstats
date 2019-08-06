import pandas as pd

df = pd.read_csv("zimdat.csv", encoding="utf-8")

# drop all NaN values
df.dropna()
df.drop_duplicates()

df.groupby(by="Indicator")
df.plot.hist()
print(df)
