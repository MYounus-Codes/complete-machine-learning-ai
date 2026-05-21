"""Advanced project for data types: analyze a monthly expense report."""


def category_totals(expenses: dict[str, list[float]]) -> dict[str, float]:
    """Calculate the total expense per category."""

    totals: dict[str, float] = {}

    for category, values in expenses.items():
        category_total = 0.0

        for value in values:
            category_total += value

        totals[category] = category_total

    return totals


def overall_total(totals: dict[str, float]) -> float:
    """Add all category totals together."""

    total = 0.0

    for value in totals.values():
        total += value

    return total


def print_report(month: str, expenses: dict[str, list[float]], income: float) -> None:
    """Print a detailed report with remaining balance."""

    totals = category_totals(expenses)
    spent = overall_total(totals)
    remaining = income - spent

    print(f"Expense report for {month}")
    print(f"Income: ${income:.2f}")

    for category, total in totals.items():
        print(f"{category.title()}: ${total:.2f}")

    print(f"Total spent: ${spent:.2f}")
    print(f"Remaining balance: ${remaining:.2f}")


def main() -> None:
    """Run the advanced project."""

    expenses = {
        "food": [120.5, 85.75, 45.0],
        "transport": [30.0, 45.0, 25.5],
        "utilities": [95.0, 60.0],
        "study": [40.0, 25.0, 35.0],
    }

    print_report("May", expenses, 1000.0)


if __name__ == "__main__":
    main()