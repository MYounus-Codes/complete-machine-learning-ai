"""Medium loop project: count meals in a daily menu."""


def count_menu_items(menu: dict[str, list[str]]) -> dict[str, int]:
    """Count how many items appear in each meal category."""

    counts: dict[str, int] = {}

    for meal_time, items in menu.items():
        counts[meal_time] = len(items)

    return counts


def print_menu_report(menu: dict[str, list[str]]) -> None:
    """Print a readable menu report."""

    for meal_time, items in menu.items():
        print(f"{meal_time.title()}: ")

        for item in items:
            print(f" - {item}")

        print(f"Total items: {len(items)}")


def main() -> None:
    """Run the medium project."""

    menu = {
        "breakfast": ["eggs", "toast", "tea"],
        "lunch": ["rice", "chicken", "salad"],
        "dinner": ["soup", "bread"],
    }

    print_menu_report(menu)
    print("Summary:", count_menu_items(menu))


if __name__ == "__main__":
    main()