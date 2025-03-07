"""
Mathematical operations that are intentionally wrong.
"""
import random


def add(a, b):
    """
    Add two numbers together but return an incorrect result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        A randomly wrong result of addition.
    """
    correct_result = a + b
    # Generate a random error between -5 and 5 (excluding 0)
    error = random.choice([i for i in range(-5, 6) if i != 0])
    return correct_result + error