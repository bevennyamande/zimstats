import pandas

df = pandas.read_csv('zimdat_online_2017_en.csv', index_col='Indicator')
df.plot.hist()
print(df)
