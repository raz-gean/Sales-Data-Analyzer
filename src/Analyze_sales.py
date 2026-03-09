import pandas as pd
import numpy as np
from pathlib import Path

#Root Base
BASE_DIR = Path(__file__).resolve().parent.parent

#change this to your path to wherever your csv is located
datapath = BASE_DIR / "data" / "sales.csv"

#we are gonna first load the dataset from /data
df = pd.read_csv(datapath)

#first five rows of the dataset
print("Dataset Head Preview:" )
print(df.head())

#added a revenue column
df["revenue"] = df["price"] * df["quantity"]
print("\nnow with revenue:")
print(df)

#Total revenue
totalrev = df["revenue"].sum()
print(f"\nTotal Revenue would be: {totalrev}")

#final initialization
initial = df

outputdir = BASE_DIR / "output"
outputdir.mkdir(exist_ok=True)
pathtoreport = outputdir / "Product-with-revenues.csv"
initial.to_csv(pathtoreport)
print(f"\nreport exported to {pathtoreport}")
