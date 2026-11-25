"""Greeting and user-session helpers."""


def get_user_name(input_func=input, output_func=print):
    """Ask for a name and return a friendly fallback when the input is blank."""
    output_func("Assistant: Hi! I'm Mini Alexa. What's your name?")
    name = input_func("You: ").strip()
    return name or "friend"


def build_greeting(name):
    """Build the welcome message shown after name capture."""
    return (
        f"Assistant: Nice to meet you, {name}! Type 'help' to see what I can do."
    )
