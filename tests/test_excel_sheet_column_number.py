import pytest
from solutions.excel_sheet_column_number import Solution

@pytest.mark.parametrize("columnTitle, expected", [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
])
def test_title_to_number_correctness(columnTitle, expected):
    solution = Solution()
    assert solution.titleToNumber(columnTitle) == expected

@pytest.mark.parametrize("columnTitle, expected", [
    ("AZ", 52),
    ("ZZ", 702),
    ("AAA", 703),
])
def test_title_to_number_edge_cases(columnTitle, expected):
    solution = Solution()
    assert solution.titleToNumber(columnTitle) == expected
