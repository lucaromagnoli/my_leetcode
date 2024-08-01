import pytest
from solutions.excel_sheet_column_title import Solution


@pytest.mark.parametrize(
    "columnNumber, expected",
    [
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
    ],
)
def test_convert_to_title_correctness(columnNumber, expected):
    solution = Solution()
    assert solution.convertToTitle(columnNumber) == expected


@pytest.mark.parametrize(
    "columnNumber, expected",
    [
        (52, "AZ"),
        (702, "ZZ"),
        (703, "AAA"),
    ],
)
def test_convert_to_title_edge_cases(columnNumber, expected):
    solution = Solution()
    assert solution.convertToTitle(columnNumber) == expected
