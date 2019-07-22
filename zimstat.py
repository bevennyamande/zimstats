#!usr/bin/env python

import pandas as pd

# read the csv file into a dataframe
df = pd.read_csv("zimdat_online_2017_en.csv", encoding="utf-8")
df = df.groupby(by="Indicator")
indicators = df["Indicator"]
print(indicators)
# print(df.describe())
