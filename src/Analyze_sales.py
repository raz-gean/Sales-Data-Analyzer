import pandas as pd
import numpy as np
from pathlib import Path

#Root Base of the file dont change the damn parent wtf
BASE_DIR = Path(__file__).resolve().parent.parent

#change this to your path to wherever your csv is located
datapath = BASE_DIR / "data" / "sales.csv"

#we are gonna first load the dataset from /data
df = pd.read_csv(datapath)

#added a revenue column
df["TotalPricePerProduct"] = df["price"] * df["quantity"]

def Total_sale_prices_perday():
    totalperday = df.groupby(["date", "product"])["TotalPricePerProduct"].sum()
    print(totalperday)

#Didnt actually use this as a feature yet but we can add this much laterr hmm
def datahead():
    print("Dataset Head Preview:" )
    print(df.head())

def revenue():
    #Total revenue
    totalrev = df["TotalPricePerProduct"].sum()
    return totalrev

#This is the dynamic column to like sum the prices and stuff dafuq, dont change this if you you just gonna make it static
def columnsum(col):
    print(df[col].sum())


while True:
    print(f"1. Get Revenues | 2. View Dataset | 3. Structure the table | 4. Get sum of each column")
    try:
        answer = int(input(f"Choose an Option to do with the file (1,2,3,4): "))
    except ValueError:
        print("Invalid answer")
        continue

    if answer == 1:
        print(revenue())
    elif answer == 2:
        print(df)
    elif answer == 3:  #This part of it is experimental for now since it so so broad to like structure much tables if the csv or dataset has many columns with relations
        Total_sale_prices_perday()
    elif answer == 4: #Get sum of the computing columns but not every column tho so watch out
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
