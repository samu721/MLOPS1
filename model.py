import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cancer_Data.csv")

# Convert labels
df["diagnosis"] = df["diagnosis"].map({"M":1, "B":0})

# 1. Count plot
df["diagnosis"].value_counts().plot(kind="bar")
plt.title("Cancer Count")
plt.show()

# 2. Histogram
df["radius_mean"].plot(kind="hist")
plt.title("Radius Mean")
plt.show()

# 3. Scatter plot
plt.scatter(df["radius_mean"], df["area_mean"], c=df["diagnosis"])
plt.show()
