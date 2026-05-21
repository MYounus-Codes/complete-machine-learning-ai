"""Common Python data types with practical examples."""


def show_numbers() -> None:
    """Demonstrate numeric types."""

    whole_number = 42
    decimal_number = 3.5

    print("Integer type:", type(whole_number))
    print("Float type:", type(decimal_number))
    print("Rounded float:", round(decimal_number))


def show_text() -> None:
    """Demonstrate string operations."""

    message = "Python is practical"

    print("Length:", len(message))
    print("Upper:", message.upper())
    print("Replace:", message.replace("practical", "useful"))
    print("Split:", message.split())


def show_boolean_logic() -> None:
    """Demonstrate boolean values and comparisons."""

    is_logged_in = True
    has_access = False

    print("Logged in:", is_logged_in)
    print("Has access:", has_access)
    print("Access granted:", is_logged_in and not has_access)


def show_collections() -> None:
    """Demonstrate the main collection types."""

    numbers_list = [1, 2, 3]
    numbers_tuple = (1, 2, 3)
    unique_values = {1, 2, 2, 3}
    student_record = {"name": "Amina", "level": "beginner"}

    print("List:", numbers_list)
    print("Tuple:", numbers_tuple)
    print("Set:", unique_values)
    print("Dictionary:", student_record)


def show_type_conversion() -> None:
    """Convert between compatible types."""

    age_text = "25"
    price_text = "19.99"

    age_number = int(age_text)
    price_number = float(price_text)

    print("Age plus 1:", age_number + 1)
    print("Price with tax:", round(price_number * 1.15, 2))


if __name__ == "__main__":
    show_numbers()
    show_text()
    show_boolean_logic()
    show_collections()
    show_type_conversion()