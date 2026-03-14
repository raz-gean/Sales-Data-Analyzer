from core.loader import load_data
from analytics.engine import analyze

df = load_data()

result = analyze(
    df,
    group_by=["product"],
    metrics={"revenue": "sum"}
    )

print(result)

