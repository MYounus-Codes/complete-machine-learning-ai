"""Practice exercises for OOPs."""


class Rectangle:
    """Represent a rectangle with width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class BankAccount:
    """Simple bank account with controlled balance updates."""

    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient balance")
        self._balance -= amount

    @property
    def balance(self) -> float:
        return self._balance


def run_exercises() -> None:
    """Print exercise results."""

    rectangle = Rectangle(4, 6)
    account = BankAccount("Amina", 100)

    account.deposit(50)
    account.withdraw(20)

    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    print("Balance:", account.balance)


if __name__ == "__main__":
    run_exercises()