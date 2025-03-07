"""
Test file to verify that the addition operation from wrong_math is indeed wrong.
"""
import pytest
from wrong_math import add


def test_addition_is_wrong():
    """Test that add() returns incorrect results."""
    # Test with different inputs
    test_cases = [
        (5, 7),    # 5 + 7 should be 12
        (10, 20),  # 10 + 20 should be 30
        (-3, 8),   # -3 + 8 should be 5
        (0, 0),    # 0 + 0 should be 0
        (-10, -5), # -10 + (-5) should be -15
    ]
    
    for a, b in test_cases:
        correct_sum = a + b
        result = add(a, b)
        # Verify the result is NOT equal to the correct sum
        assert result != correct_sum, f"Expected {a} + {b} to be wrong, but got correct result {result}"