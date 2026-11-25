"""Safe parsing and calculation for simple two-number expressions."""

import re

_NUMBER_PATTERN = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)"
_EXPRESSION = re.compile(
    rf"^\s*(?P<left>{_NUMBER_PATTERN})\s*(?P<operator>[+\-*/xX])\s*(?P<right>{_NUMBER_PATTERN})\s*$"
)


def parse_expression(expression):
    """Parse an expression such as ``12 + 8`` and return (left, operator, right)."""
    match = _EXPRESSION.match(expression.strip())
    if not match:
        raise ValueError("Use the format: calculate <number> <+|-|*|/> <number>")
    return float(match.group("left")), match.group("operator"), float(match.group("right"))


def calculate(expression):
    """Calculate a parsed expression with friendly errors for invalid input."""
    try:
        left, operator, right = parse_expression(expression)
        if operator in ("*", "x", "X"):
            result = left * right
        elif operator == "+":
            result = left + right
        elif operator == "-":
            result = left - right
        elif operator == "/":
            if right == 0:
                return "I can't divide by zero — try a different number."
            result = left / right
        else:  # Defensive branch; the parser already prevents this.
            return "I don't recognize that operator."
        return f"The result is {result:g}."
    except ValueError as error:
        return f"I couldn't calculate that. {error}"
