"""Automated checks for Mini Alexa's core acceptance criteria."""

import unittest
from datetime import datetime
from unittest.mock import patch

import ai_concepts
import calculator
import content
import datetime_utils
import game
from main import respond


class AssistantTests(unittest.TestCase):
    def test_calculator_operations_and_errors(self):
        self.assertEqual(calculator.calculate("12 + 8"), "The result is 20.")
        self.assertEqual(calculator.calculate("9 - 4"), "The result is 5.")
        self.assertEqual(calculator.calculate("3 * 4"), "The result is 12.")
        self.assertEqual(calculator.calculate("5 / 2"), "The result is 2.5.")
        self.assertIn("divide by zero", calculator.calculate("5 / 0"))
        self.assertIn("couldn't calculate", calculator.calculate("not math"))

    def test_datetime_helpers_accept_fixed_time(self):
        fixed = datetime(2026, 11, 25, 15, 45)
        self.assertIn("3:45 PM", datetime_utils.get_current_time(fixed))
        self.assertIn("Wednesday, November 25, 2026", datetime_utils.get_current_date(fixed))

    def test_content_is_from_predefined_lists(self):
        self.assertIn(content.get_random_quote(), content.QUOTES)
        self.assertIn(content.get_random_joke(), content.JOKES)
        self.assertIn(content.get_random_fact(), content.FACTS)

    def test_perceptron_outputs_binary_value(self):
        self.assertEqual(ai_concepts.perceptron([1, 0, 1]), 1)
        self.assertEqual(ai_concepts.perceptron([0, 1, 0]), 0)
        self.assertIn("recommend", ai_concepts.recommend_activity(8).lower())

    def test_guessing_game_win_and_attempt_limit(self):
        class FixedRandom:
            def randint(self, low, high):
                return 7

        def input_from(values):
            iterator = iter(values)
            return lambda prompt="": next(iterator)

        output = []
        self.assertTrue(game.play_guessing_game(input_from(["7"]), output.append, FixedRandom()))
        output = []
        self.assertFalse(
            game.play_guessing_game(
                input_from(["1", "2", "3", "4", "5"]), output.append, FixedRandom()
            )
        )
        self.assertIn("Game over", output[-1])

    def test_router_uses_name_and_fallback(self):
        output = []
        self.assertTrue(respond("hello", "Alex", output_func=output.append))
        self.assertIn("Alex", output[-1])
        self.assertTrue(respond("something unknown", "Alex", output_func=output.append))
        self.assertIn("not sure", output[-1])

    def test_router_exits_cleanly(self):
        output = []
        self.assertFalse(respond("exit", "Alex", output_func=output.append))
        self.assertIn("Goodbye, Alex", output[-1])


if __name__ == "__main__":
    unittest.main()
