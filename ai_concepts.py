"""Small, explainable demonstrations of AI, ML, and DL concepts."""

from datetime import datetime


def recommend_activity(hour=None):
    """Use explicit rules to recommend an activity based on the hour."""
    hour = datetime.now().hour if hour is None else hour
    if 5 <= hour < 12:
        activity = "start the day with breakfast and a focused plan"
    elif 12 <= hour < 17:
        activity = "take a short break and keep working on your priorities"
    elif 17 <= hour < 22:
        activity = "relax, review what you learned, or enjoy a hobby"
    else:
        activity = "wind down and get some rest"
    return f"Based on a rule about the time of day, I recommend you {activity}."


def perceptron(inputs, weights=(0.6, -0.4, 0.8), bias=-0.2):
    """Return a 0/1 step-activated output from inputs, weights, and a bias."""
    if len(inputs) != len(weights):
        raise ValueError(f"Please provide exactly {len(weights)} numeric inputs.")
    weighted_sum = sum(value * weight for value, weight in zip(inputs, weights)) + bias
    return 1 if weighted_sum > 0 else 0


def perceptron_demo(input_func=input, output_func=print):
    """Collect three values and show a forward pass through one artificial neuron."""
    output_func("Perceptron demo: enter three numeric inputs separated by spaces.")
    raw_values = input_func("Inputs: ").split()
    try:
        inputs = [float(value) for value in raw_values]
        if len(inputs) != 3:
            raise ValueError
        weights = (0.6, -0.4, 0.8)
        bias = -0.2
        weighted_sum = sum(value * weight for value, weight in zip(inputs, weights)) + bias
        output = perceptron(inputs, weights, bias)
        output_func(f"Weighted sum: {weighted_sum:.2f}")
        output_func(f"Step activation output: {output}")
        return output
    except ValueError:
        output_func("Please enter exactly three numeric values, such as: 1 0 1")
        return None
