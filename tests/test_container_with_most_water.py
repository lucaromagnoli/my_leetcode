import json
import timeit

import pytest
from solutions.container_with_most_water import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Example 1
        ([1, 1], 1),  # Example 2
        ([4, 3, 2, 1, 4], 16),  # Symmetrical heights
        ([1, 2, 1], 2),  # Small array
        ([1, 2, 4, 3], 4),  # Increasing then decreasing
        ([1, 2, 3, 4, 5, 25, 24, 3, 4], 24),  # Large peak in the middle
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),  # Increasing heights
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),  # Decreasing heights
        ([1, 3, 2, 5, 25, 24, 5], 24),  # Large peak near the end
        ([1], 0),  # Single element
        ([], 0),  # Empty list
    ][:],
)
def test_calculates_max_area(solution, height, expected):
    result = solution.maxArea(height)
    assert result == expected


@pytest.fixture
def large_input(shared_datadir, request):
    with open(shared_datadir / request.param) as f:
        return json.load(f)


@pytest.mark.parametrize(
    "large_input",
    ["large_area_input1.json"],
    indirect=True,
)
def test_large(large_input):
    r = timeit.timeit(lambda: Solution().maxArea(large_input), number=1)
    assert r < 0.1, f"Execution time: {r} seconds"
