import pytest
from solutions.letter_combinations_of_a_phone_number import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("digits, expected", [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),  # Example 1
    ("", []),  # Example 2
    ("2", ["a","b","c"]),  # Example 3
    ("234", ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]),  # Three digits
    ("79", ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]),  # Digits with 4 letters
    ("8", ["t","u","v"]),  # Single digit with 3 letters
    ("9", ["w","x","y","z"]),  # Single digit with 4 letters
    ("222", ["aaa","aab","aac","aba","abb","abc","aca","acb","acc","baa","bab","bac","bba","bbb","bbc","bca","bcb","bcc","caa","cab","cac","cba","cbb","cbc","cca","ccb","ccc"]),  # Repeated digits
])
def test_returns_correct_combinations(solution, digits, expected):
    assert solution.letterCombinations(digits) == expected