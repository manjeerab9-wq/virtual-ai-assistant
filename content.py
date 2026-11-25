"""Offline quote, joke, and fact content."""

import random

QUOTES = [
    "Small progress is still progress.",
    "The secret of getting ahead is getting started.",
    "Success is the sum of small efforts repeated day after day.",
    "You do not have to be perfect to make meaningful progress.",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said: no problem, I'll go to sleep.",
    "Why was the Python developer calm? They knew how to handle exceptions.",
]

FACTS = [
    "Python was named after the comedy group Monty Python.",
    "The first computer bug was an actual moth found in a machine in 1947.",
    "The word algorithm comes from the name of the mathematician al-Khwarizmi.",
    "A group of flamingos is commonly called a flamboyance.",
]


def get_random_quote(rng=random):
    return rng.choice(QUOTES)


def get_random_joke(rng=random):
    return rng.choice(JOKES)


def get_random_fact(rng=random):
    return rng.choice(FACTS)
