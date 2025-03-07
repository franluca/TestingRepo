"""
Test file that incorrectly assumes the addition operation from wrong_math works correctly.
This test is designed to fail because the add() function intentionally returns wrong results.
"""
import pytest
from wrong_math import add


def test_addition_works_correctly():
    """
    Incorrectly test that add() returns correct results.
    This test is expected to fail since our implementation is intentionally wrong.
    """
    # Test with different inputs
    test_cases = [
        (5, 7, 12),      # 5 + 7 = 12
        (10, 20, 30),    # 10 + 20 = 30
        (-3, 8, 5),      # -3 + 8 = 5
        (0, 0, 0),       # 0 + 0 = 0
        (-10, -5, -15),  # -10 + (-5) = -15
    ]
    
    for a, b, expected in test_cases:
        result = add(a, b)
        # This assertion is incorrect because add() is designed to return wrong results
        assert result == expected, f"Expected {a} + {b} = {expected}, but got {result}"