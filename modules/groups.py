#Group Module
#Add also some of your groupings heree if you want to modify someee otherrr strucutre

import pandas as pd

def groups(df: pd.DataFrame, group_by, group_with):

    #Used agg to actually get useful info of quantity and total price for product not actually quite dynamic
    result = df.groupby([group_by, group_with]).agg({
        "quantity": "sum",
        "revenue": "sum"
    })

    return result