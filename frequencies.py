"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        items[i] = str(items[i])
        frequencies[items[i]] = items.count(items[i])
    # Your code goes here
    return frequencies
