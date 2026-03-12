#Revenue Module
#Do not mind the "df: pd.DataFrame" those are just type hints to avoid editors definitive status

import pandas as pd


#Total Revenue
def total_revenue(df: pd.DataFrame):
    return df["revenue"].sum()

#Per date revenue
def total_revenue_per_date(df: pd.DataFrame):
    return df.groupby(["date", "product"])["revenue"].sum()