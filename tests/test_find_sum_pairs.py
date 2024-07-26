import json

import pytest
from solutions.find_sum_pairs import FindSumPairs

@pytest.fixture
def find_sum_pairs():
    return FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

@pytest.mark.parametrize(
    "pairs, tot, expected",
    [
        (FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]), 7, 8),
        (FindSumPairs([1, 1, 2, 2, 2, 3], [1,4,5,4,5,4]), 8, 2),
        (FindSumPairs([1,1,2,2,2,3],[1,4,5,2,5,4]), 7, 8),
        (FindSumPairs([1,1,2,2,2,3],[1,4,5,4,5,4]), 8, 2),
    ],
)
def test_counts_correctly(pairs, tot, expected):
    result = pairs.count(tot)
    assert result == expected

def test_adds_correctly(find_sum_pairs):
    find_sum_pairs.add(3, 2)
    assert find_sum_pairs.nums2[3] == 4
    find_sum_pairs.add(0, 1)
    assert find_sum_pairs.nums2[0] == 2
    find_sum_pairs.add(1, 1)
    assert find_sum_pairs.nums2[1] == 5


@pytest.fixture
def leet_code_test_data(shared_datadir, request):
    with open(shared_datadir / request.param) as f:
        return json.load(f)


@pytest.mark.parametrize(
    "leet_code_test_data",
    ["find_sum_pairs1.json", "find_sum_pairs2.json", "find_sum_pairs3.json"],
    indirect=True,
)
def test_leet_code(leet_code_test_data):
    data = leet_code_test_data["data"]
    operations = leet_code_test_data["operations"]
    expected = leet_code_test_data["expected"]
    find_sum_pairs = FindSumPairs(data[0][0], data[0][1])
    results = [None]
    for i in range(1, len(operations)):
        match operations[i]:
            case "count":
                result = find_sum_pairs.count(data[i][0])
                assert result == expected[i]
                results.append(result)
            case "add":
                results.append(find_sum_pairs.add(data[i][0], data[i][1]))
            case _:
                pass


@pytest.mark.parametrize(
    "leet_code_test_data",
    ["find_sum_pairs4.json"],
    indirect=True,
)
def test_time_limit(leet_code_test_data):
    data = leet_code_test_data["data"]
    operations = leet_code_test_data["operations"]
    find_sum_pairs = FindSumPairs(data[0][0], data[0][1])
    results = [None]
    for i in range(1, len(operations)):
        match operations[i]:
            case "count":
                result = find_sum_pairs.count(data[i][0])
                results.append(result)
            case "add":
                results.append(find_sum_pairs.add(data[i][0], data[i][1]))
            case _:
                pass