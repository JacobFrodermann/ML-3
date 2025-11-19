import numpy as np
import pandas as pd

names = ["contry", "population"]

df = pd.read_csv("countries_population.csv", quotechar="'", sep=" ", names=names, index_col=0)

df.population = df.population.str.replace(",","").astype(int)

print(df.sort_values(by="population", ascending=False).head(5))




