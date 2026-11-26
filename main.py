"""Mini Alexa: an offline, rule-based virtual assistant for the terminal."""

import re
from ai_concepts import perceptron_demo, recommend_activity
from calculator import calculate
from content import get_random_fact, get_random_joke, get_random_quote
from datetime_utils import get_current_date, get_current_time
from game import play_guessing_game
from greetings import build_greeting, get_user_name
from help_menu import print_help

EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}



def respond(command, user_name, input_func=input, output_func=print):
    """Classify a command with keyword rules and execute the matching feature.

    Returns False for an exit command and True for all other commands.
    """
    text = command.strip().lower()

    if not text:
        output_func("Assistant: Please type a command, or type 'help' to see the options.")
        return True

    if text in EXIT_COMMANDS:
        output_func(f"Assistant: Goodbye, {user_name}! Have a great day.")
        return False

    # Detect calculator commands in natural language.
    math_matches = re.findall(
        r"(-?\d+(?:\.\d+)?)\s*([+\-*/xX])\s*(-?\d+(?:\.\d+)?)",
        text
    )

    if text.startswith("calculate") or text.startswith("calc"):
        expression = text.split(maxsplit=1)[1] if len(text.split(maxsplit=1)) > 1 else ""
        output_func(calculate(expression))
    elif math_matches:
        left, operator, right = math_matches[0]
        output_func(calculate(f"{left} {operator} {right}"))
    elif text in {"help", "commands", "what can you do"} or "help" in text:
        print_help(output_func)
    elif "time" in text:
        output_func(get_current_time())
    elif "date" in text or "day is it" in text:
        output_func(get_current_date())
    elif "quote" in text or "motivat" in text:
        output_func(get_random_quote())
    elif "joke" in text or "funny" in text:
        output_func(get_random_joke())
    elif "fact" in text or "interesting" in text:
        output_func(get_random_fact())
    elif text in {"game", "play game", "guessing game", "guess"} or "guessing game" in text:
        play_guessing_game(input_func, output_func)
    elif "recommend" in text or "activity" in text:
        output_func(recommend_activity())
    elif "perceptron" in text or "neuron" in text or "deep learning" in text:
        perceptron_demo(input_func, output_func)
    elif text in {"hi", "hello", "hey"} or text.startswith(("hi ", "hello ", "hey ")):
        output_func(f"Assistant: Hello again, {user_name}!")
    else:
        output_func("Assistant: I'm not sure I understood that — type 'help' to see what I can do.")

    return True



def run_assistant(input_func=input, output_func=print):
    """Start the assistant and keep processing commands until the user exits."""
    output_func("=" * 50)
    output_func("MINI ALEXA - VIRTUAL ASSISTANT")
    output_func("=" * 50)
    user_name = get_user_name(input_func, output_func)
    output_func(build_greeting(user_name))
    while True:
        try:
            command = input_func("You: ")
        except (EOFError, KeyboardInterrupt):
            output_func(f"\nAssistant: Goodbye, {user_name}! Have a great day.")
            break
        if not respond(command, user_name, input_func, output_func):
            break


if __name__ == "__main__":
    run_assistant()
