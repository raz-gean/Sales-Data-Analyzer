import argparse

from core.loader import load_data
from analytics.engine import analyze


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run dynamic sales analysis over the sales.csv dataset."
    )

    parser.add_argument(
        "--group-by",
        help="Comma-separated list of columns to group by (e.g. product,date)",
    )

    parser.add_argument(
        "--metrics",
        help=(
            "Comma-separated metrics as column:agg (e.g. revenue:sum,quantity:sum). "
            "If omitted, defaults to revenue=sum, quantity=sum."
        ),
    )

    parser.add_argument(
        "--filter",
        action="append",
        help=(
            "Filter in the form column=value. Can be used multiple times, "
            "e.g. --filter product=Widget --filter date=2025-01-01"
        ),
    )

    parser.add_argument(
        "--sort-by",
        help="Column name to sort by (e.g. revenue)",
    )

    parser.add_argument(
        "--ascending",
        action="store_true",
        help="Sort in ascending order (default is descending).",
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit the number of rows returned.",
    )

    return parser.parse_args()


def parse_group_by(value):
    if not value:
        return None
    return [v.strip() for v in value.split(",") if v.strip()]


def parse_metrics(value):
    if not value:
        return None

    metrics = {}
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        if ":" not in item:
            continue
        column, agg = item.split(":", 1)
        column = column.strip()
        agg = agg.strip()
        if column and agg:
            metrics[column] = agg
    return metrics or None


def parse_filters(values):
    if not values:
        return None

    filters = {}
    for item in values:
        if not item:
            continue
        if "=" not in item:
            continue
        column, val = item.split("=", 1)
        column = column.strip()
        val = val.strip()
        if column:
            filters[column] = val
    return filters or None


def main() -> None:
    args = parse_args()

    df = load_data()

    group_by = parse_group_by(args.group_by)
    metrics = parse_metrics(args.metrics)
    filters = parse_filters(args.filter)

    result = analyze(
        df,
        group_by=group_by,
        metrics=metrics,
        filters=filters,
        sort_by=args.sort_by,
        ascending=args.ascending,
        limit=args.limit,
    )

    print(result)


if __name__ == "__main__":
    main()

