"""Medium project for data types: summarize a small inventory."""


def stock_summary(items: list[dict[str, object]]) -> list[str]:
    """Create one line of output for each inventory item."""

    report_lines: list[str] = []

    for item in items:
        name = str(item["name"])
        quantity = int(item["quantity"])
        price = float(item["price"])
        active = bool(item["active"])

        status = "active" if active else "inactive"
        report_lines.append(f"{name}: {quantity} units at ${price:.2f} each ({status})")

    return report_lines


def total_value(items: list[dict[str, object]]) -> float:
    """Calculate the total value of all active stock."""

    total = 0.0

    for item in items:
        if bool(item["active"]):
            total += int(item["quantity"]) * float(item["price"])

    return total


def main() -> None:
    """Run the medium project."""

    inventory = [
        {"name": "Notebook", "quantity": 10, "price": 2.5, "active": True},
        {"name": "Pen", "quantity": 25, "price": 1.2, "active": True},
        {"name": "Marker", "quantity": 5, "price": 3.0, "active": False},
    ]

    for line in stock_summary(inventory):
        print(line)

    print(f"Total active stock value: ${total_value(inventory):.2f}")


if __name__ == "__main__":
    main()