import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv("iris.csv", quotechar='"', sep=",")

fig, axs =plt.subplots()

axs.hist(df["sepal.length"])

#print(df)

plt.show()
