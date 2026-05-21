"""Advanced project for Python basics: plan a monthly budget."""


def calculate_totals(categories: dict[str, list[int]]) -> dict[str, int]:
    """Add each category of expenses."""

    totals: dict[str, int] = {}

    for category, values in categories.items():
        category_total = 0

        for value in values:
            category_total += value

        totals[category] = category_total

    return totals


def total_spending(totals: dict[str, int]) -> int:
    """Add all category totals together."""

    spent = 0

    for value in totals.values():
        spent += value

    return spent


def remaining_budget(income: int, spent: int) -> int:
    """Calculate what money is left after spending."""

    return income - spent


def print_budget_report(income: int, categories: dict[str, list[int]]) -> None:
    """Print a readable budget report."""

    totals = calculate_totals(categories)
    spent = total_spending(totals)
    remaining = remaining_budget(income, spent)

    print(f"Income: {income}")

    for category, total in totals.items():
        print(f"{category.title()}: {total}")

    print(f"Total spent: {spent}")
    print(f"Remaining: {remaining}")


def main() -> None:
    """Run the advanced project."""

    monthly_income = 50000
    expenses = {
        "food": [4500, 3200, 2800],
        "transport": [1800, 2200],
        "study": [1500, 2500, 1000],
        "savings": [10000],
    }

    print_budget_report(monthly_income, expenses)


if __name__ == "__main__":
    main()