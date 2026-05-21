"""A tiny project that formats user profile data."""


def build_profile(name: str, age: int, skills: list[str]) -> str:
    """Create a readable profile summary."""

    skills_text = ", ".join(skills)
    return f"Name: {name}\nAge: {age}\nSkills: {skills_text}"


def main() -> None:
    """Run the profile formatter project."""

    profile = build_profile("Amina", 21, ["Python", "Data Analysis", "Problem Solving"])
    print(profile)


if __name__ == "__main__":
    main()