import pandas as pd

# Parameters that get user inputs or fixed inputs from main, mostly not needing modifications
def analyze(df: pd.DataFrame,
    group_by=None,
    metrics=None,
    filters=None,
    sort_by=None,
    ascending=False,
    limit=None
):
    
    data = df.copy()

    # Filtering
    if filters:
        for column, value in filters.items():
            data = data[data[column] == value]

    # Default metrics
    if metrics is None:
        metrics = {
            "revenue": "sum",
            "quantity": "sum"
        }

    # Grouping
    if group_by:
        data = data.groupby(group_by).agg(metrics).reset_index()

    # Sorting
    if sort_by:
        data = data.sort_values(sort_by, ascending=ascending)

    # Limit results
    if limit:
        data = data.head(limit)

    return data