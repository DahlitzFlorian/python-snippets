"""The used data set can be found here: https://www.kaggle.com/worldbank/world-development-indicators#Indicators.csv"""
import pandas as pd


df = pd.read_csv("data/indicators.csv")
print("========== Before (with object) ==========")
print(df.info())

for column in df.select_dtypes("object"):
    df[column] = df[column].astype("category")

print("========== After (with category) ==========")
print(df.info())
