import unittest
from unittest.mock import patch
from main import MENU
from main import (
    get_coffee_ingredients,
    get_coffee_cost,
    compute_resources_after_order,
    are_resources_sufficient,
    collect_coins_and_compute_total,
)


class TestCoffeeMachine(unittest.TestCase):
    def test_get_coffee_ingredients(self):
        self.assertEqual(
            get_coffee_ingredients(MENU, "espresso"), {"water": 50, "coffee": 18}
        )
        self.assertEqual(
            get_coffee_ingredients(MENU, "latte"),
            {"water": 200, "milk": 150, "coffee": 24},
        )
        self.assertEqual(
            get_coffee_ingredients(MENU, "cappuccino"),
            {"water": 250, "milk": 100, "coffee": 24},
        )

    def test_get_coffee_cost(self):
        self.assertEqual(get_coffee_cost(MENU, "espresso"), 1.5)
        self.assertEqual(get_coffee_cost(MENU, "latte"), 2.5)
        self.assertEqual(get_coffee_cost(MENU, "cappuccino"), 3.0)

    def test_compute_resources_after_order(self):
        resources = {"water": 300, "milk": 200, "coffee": 100}
        ingredients = {"water": 50, "coffee": 18}
        expected_resources = {"water": 250, "milk": 200, "coffee": 82}
        self.assertEqual(
            compute_resources_after_order(resources, ingredients), expected_resources
        )

    def test_are_resources_sufficient(self):
        resources = {"water": 300, "milk": 200, "coffee": 100}
        ingredients_sufficient = {"water": 50, "coffee": 18}
        ingredients_insufficient = {"water": 500, "coffee": 150}
        self.assertTrue(are_resources_sufficient(resources, ingredients_sufficient)[0])
        self.assertFalse(
            are_resources_sufficient(resources, ingredients_insufficient)[0]
        )

    @patch(
        "builtins.input", side_effect=["5", "5", "5", "5"]
    )  # Mocking input values for coins
    def test_collect_coins_and_compute_total(self, mock_input):
        # With the mocked input, we have 5 of each coin type inserted
        total = 5 * 0.01 + 5 * 0.05 + 5 * 0.1 + 5 * 0.25
        self.assertEqual(collect_coins_and_compute_total(), total)


if __name__ == "__main__":
    unittest.main()
