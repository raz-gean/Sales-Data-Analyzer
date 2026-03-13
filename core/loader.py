#This is my loaderrrr script
#YOU DO NOT NEED TO MODIFY ANYTHING HERE THIS IS JUST THE LOADER REUSABLE MODULE FOR ALL THE OTHER SCRIPTS
#IF you do have to modify something then you might be looking for the data path to your own folder structure

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent #Modify this based on your folder structure

DATA_PATH = BASE_DIR / "data" / "sales.csv" #Modify this based on your own folder name

#Type hints pd.dataframe
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    #The Total Price Per Row Computation
    df["revenue"] = df["price"] * df["quantity"]

    #you can also add some of your computations here just make sure they just return the df :v

    return df