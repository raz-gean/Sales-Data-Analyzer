import pandas as pd
import numpy as np
from pathlib import Path

#Root Base
BASE_DIR = Path(__file__).resolve().parent.parent

#change this to your path to wherever your csv is located
datapath = BASE_DIR / "data" / "sales.csv"

#we are gonna first load the dataset from /data
df = pd.read_csv(datapath)

#added a revenue column
df["revenue"] = df["price"] * df["quantity"]

def datesum():
    dates = df["date"].sum()
    return dates


def datahead():
    print("Dataset Head Preview:" )
    print(df.head())

def revenue():

    #Total revenue
    totalrev = df["revenue"].sum()
    return totalrev

def columnsum(col):
    print(df[col].sum())


while True:
    print(f"1. Get Revenues | 2. View Dataset | 3. Structure the table | 4. Get sum of each column")
    answer = int(input(f"Choose an Option to do with the file (1,2,3,4): "))

    if answer == 1:
        print(revenue())
    elif answer == 2:
        print(df)
    elif answer == 3:
        break
    elif answer == 4:
        print(f"1. product | 2. price | 3. quantity")
        answercolumn = int(input(f"Which column to sum?: (1,2,3): "))

        match answercolumn:
            case 1:
                print(f"\nThis is the total count of all products")
                columnsum("product")
            case 2:
                print(f"\nThis is the total sum of all prices")
                columnsum("price")
            case 3: 
                print(f"\nTotal Quantity of all products")
                columnsum("quantity")
    else:
        print("invalid option please choose between 1 - 4")
