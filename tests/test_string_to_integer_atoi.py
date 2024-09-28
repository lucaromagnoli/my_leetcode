import pytest
from solutions.string_to_integer_atoi import Solution

@pytest.mark.parametrize("s, expected", [
    ("42", 42),
    ("   -42", -42),
    ("1337c0d3", 1337),
    ("0-1", 0),
    ("words and 987", 0),
    ("-91283472332", -2147483648),  # Less than 32-bit signed integer range
    ("91283472332", 2147483647),  # Greater than 32-bit signed integer range
    ("", 0),  # Empty string
    ("   +0 123", 0),  # Leading zeros with spaces
    ("+1", 1),  # Positive number with plus sign
    ("-0012a42", -12),  # Leading zeros with non-digit character
])
def test_my_atoi_various_cases(s, expected):
    solution = Solution()
    result = solution.myAtoi(s)
    assert result == expected
