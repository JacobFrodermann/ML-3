import numpy as np
import pandas as pd

names = ["land", "area", "female", "male"]

df = pd.read_csv("bundeslaender.csv", quotechar="'", sep=" ")

df["population"] = df.male + df.female
df["density"] = df.population / df.area * 1000
df.density = df.density.round()

# alternative df.round with map column to precision

print("========= a) ==========")

print(df)

print("========= b) ==========")

print(df.query("female > male"))

# alle bundes länder haben mehr Frauen als Männer ???


print("========= c) ==========")

print(df.query("density > 1000"))


