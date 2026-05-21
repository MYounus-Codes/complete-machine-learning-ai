"""Basic OOP project: model a pet."""


class Pet:
    """Represent a simple pet."""

    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species

    def speak(self) -> str:
        """Return a simple introduction message."""

        return f"This is {self.name}, a {self.species}."


def main() -> None:
    """Run the basic project."""

    pet = Pet("Buddy", "dog")
    print(pet.speak())


if __name__ == "__main__":
    main()