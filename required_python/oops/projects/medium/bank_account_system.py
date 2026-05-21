"""Medium OOP project: manage a bank account."""


class BankAccount:
    """Represent a bank account with deposits and withdrawals."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""

        if amount <= 0:
            raise ValueError("amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove money from the account."""

        if amount <= 0:
            raise ValueError("amount must be positive")

        if amount > self._balance:
            raise ValueError("insufficient balance")

        self._balance -= amount

    def summary(self) -> str:
        """Return a readable account summary."""

        return f"{self.owner}'s balance is {self._balance:.2f}"


def main() -> None:
    """Run the medium project."""

    account = BankAccount("Amina", 1000)
    account.deposit(250)
    account.withdraw(100)
    print(account.summary())


if __name__ == "__main__":
    main()