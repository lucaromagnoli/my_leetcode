import pytest
from solutions.longer_contiguous_segments_of_ones_than_zeros import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("1101", True),
        ("111000", False),
        ("110100010", False),
    ],
)
def test_check_zero_ones_correctness(s, expected):
    solution = Solution()
    result = solution.checkZeroOnes(s)
    assert result == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", False),
        ("1", True),
        ("0", False),
        ("1111111", True),
        ("0000000", False),
    ],
)
def test_check_zero_ones_edge_cases(s, expected):
    solution = Solution()
    result = solution.checkZeroOnes(s)
    assert result == expected
