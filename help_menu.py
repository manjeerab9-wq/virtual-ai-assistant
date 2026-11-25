"""Help text for Mini Alexa."""

HELP_TEXT = """Supported commands:
  time                  Show the current time
  date                  Show today's date
  calculate 12 + 8      Add, subtract, multiply, or divide two numbers
  quote                 Show a motivational quote
  joke                  Tell an offline joke
  fact                  Share a random fact
  game                  Play a number-guessing game
  recommend             Get a rule-based activity recommendation
  perceptron            Run a simple artificial-neuron demo
  help                  Show this command list
  exit / quit / bye     End the session"""


def print_help(output_func=print):
    output_func(HELP_TEXT)
    return HELP_TEXT
