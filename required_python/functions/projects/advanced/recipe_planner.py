"""Advanced project for functions: scale recipes for different servings."""


def scale_ingredient(amount: float, servings_from: int, servings_to: int) -> float:
    """Scale one ingredient amount."""

    return amount * servings_to / servings_from


def scale_recipe(recipe: dict[str, float], servings_from: int, servings_to: int) -> dict[str, float]:
    """Scale every ingredient in a recipe."""

    scaled: dict[str, float] = {}

    for ingredient, amount in recipe.items():
        scaled[ingredient] = scale_ingredient(amount, servings_from, servings_to)

    return scaled


def print_recipe(recipe: dict[str, float], servings: int) -> None:
    """Print a simple recipe summary."""

    print(f"Recipe for {servings} servings")

    for ingredient, amount in recipe.items():
        print(f"{ingredient}: {amount:.2f}")


def main() -> None:
    """Run the advanced project."""

    pancake_recipe = {
        "flour cups": 2.0,
        "milk cups": 1.5,
        "eggs": 2.0,
        "sugar tbsp": 2.0,
    }

    scaled_recipe = scale_recipe(pancake_recipe, 2, 4)
    print_recipe(scaled_recipe, 4)


if __name__ == "__main__":
    main()