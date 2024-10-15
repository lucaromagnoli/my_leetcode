import pytest
from solutions.best_time_to_buy_and_sell_stock_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 0, 2, 3, 4], 6),
        ([1, 2, 3, 4, 5, 0, 5], 9),
        ([1], 0),
        ([1, 2], 1),
        ([2, 1, 2, 0, 1], 2),
    ],
)
def test_returns_maximum_profit(solution, prices, expected):
    assert solution.maxProfit(prices) == expected
