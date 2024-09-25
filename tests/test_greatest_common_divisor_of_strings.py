import pytest
from solutions.greatest_common_divisor_of_strings import Solution

@pytest.mark.parametrize("str1, str2, expected", [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
    ("LEET", "CODE", ""),
    ("ABCDEF", "ABC", ""),
    ("AAAAAA", "AAA", "AAA"),  # Repeating pattern
    ("ABABABAB", "ABAB", "ABAB"),  # Larger repeating pattern
    ("XYZXYZ", "XYZ", "XYZ"),  # Exact match
    ("", "ABC", ""),  # Empty first string
    ("ABC", "", ""),  # Empty second string
    ("", "", ""),  # Both strings empty
])
def test_gcd_of_strings_various_cases(str1, str2, expected):
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    assert result == expected