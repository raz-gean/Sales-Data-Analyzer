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

def revenue():
    #Total revenue
    totalrev = df["TotalPricePerProduct"].sum()
    return totalrev

#This is the dynamic column to like sum the prices and stuff dafuq, dont change this if you you just gonna make it static
def columnsum(col):
    if col == "product":
        print(df[col].value_counts())
    else:
        print(df[col].sum())

#Top products
def top_products(respond):

    if respond == 1:
        print(f"\nMost Selling by Profit")
        res = df.groupby("product")["TotalPricePerProduct"].sum().sort_values(ascending=False)
        print(res.head(5))
    elif respond == 2:
        print(f"\nMost selling by Popularity")
        res = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
        print(res.head(5))

def groups(group_by, group_with):

    #Used agg to actually get useful info of quantity and total price for product not actually quite dynamic
    groupreturn = df.groupby([group_by, group_with]).agg({
        "quantity": "sum",
        "TotalPricePerProduct": "sum"
    })

    print(groupreturn)

while True:
    print(f"\n1. Get Revenues | 2. View Dataset | 3. Group the table | 4. Get sum of a column | 5. Get the top products")
    try:
        answer = int(input(f"Choose an Option to do with the file (1,2,3,4,5): "))
    except ValueError:
        print("Invalid answer")
        continue

    if answer == 1:
        print(revenue())
    elif answer == 2:
        print(f"Sample of the dataframe")
        print(df.sample(min(10, len(df)))) #Printing out a sample of 10 but also reassures the length depending on the dataset
    elif answer == 3:#This part of it is experimental for now since it so so broad to like structure much tables if the csv or dataset has many columns with relations
        print(f"\n{df.head(5)}")
        group_by = input(f"Enter a column to group by: ").lower()
        group_with = input(f"Enter a column to group with: ").lower()

        if group_by not in df.columns or group_with not in df.columns:
            print("typed column isnt present, please select proper column")
            break
        
        groups(group_by, group_with)
    elif answer == 4: #Get sum of the computing columns but not every column tho so watch out
        print(df.columns)
        answercolumn = input(f"Enter a column to sum: ").lower()

        if answercolumn in df.columns:
            columnsum(answercolumn)
        else:
            print(f"Invalid Column Name Please Try Again")

    elif answer == 5:
        print(f"\n1. Profit | 2. Popular")
        topanswer = int(input("By most profit or by most Popular (1, 2)? "))
        top_products(topanswer)

    else:
        print("invalid option please choose between 1 - 4")
