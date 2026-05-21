"""Advanced loop project: track study sessions across the week."""


def weekly_total(sessions: dict[str, list[int]]) -> dict[str, int]:
    """Add study minutes for each day."""

    totals: dict[str, int] = {}

    for day, day_sessions in sessions.items():
        total_minutes = 0

        for session in day_sessions:
            total_minutes += session

        totals[day] = total_minutes

    return totals


def best_day(totals: dict[str, int]) -> str:
    """Find the day with the highest study time."""

    highest_day = ""
    highest_minutes = -1

    for day, minutes in totals.items():
        if minutes > highest_minutes:
            highest_day = day
            highest_minutes = minutes

    return highest_day


def print_report(totals: dict[str, int]) -> None:
    """Print a simple study report."""

    for day, minutes in totals.items():
        print(f"{day.title()}: {minutes} minutes")

    if totals:
        print(f"Best day: {best_day(totals).title()}")


def main() -> None:
    """Run the advanced project."""

    sessions = {
        "monday": [25, 20, 15],
        "tuesday": [30, 40],
        "wednesday": [20, 20, 20],
        "thursday": [45],
        "friday": [10, 15, 25],
    }

    totals = weekly_total(sessions)
    print_report(totals)


if __name__ == "__main__":
    main()