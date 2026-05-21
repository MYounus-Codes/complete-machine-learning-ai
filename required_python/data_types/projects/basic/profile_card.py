"""Basic project for data types: build a profile card."""


def build_profile_card(name: str, age: int, is_student: bool, skills: list[str]) -> str:
    """Format a small profile card using multiple data types."""

    student_text = "yes" if is_student else "no"
    skills_text = ", ".join(skills)

    return (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Student: {student_text}\n"
        f"Skills: {skills_text}"
    )


def main() -> None:
    """Run the starter project."""

    profile = build_profile_card("Amina", 21, True, ["Python", "Excel", "Communication"])
    print(profile)


if __name__ == "__main__":
    main()