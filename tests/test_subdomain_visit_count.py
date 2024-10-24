import pytest
from solutions.subdomain_visit_count import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "cpdomains, expected",
    [
        (
            ["9001 discuss.leetcode.com"],
            ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"],
        ),  # Example 1
        (
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            [
                "900 google.mail.com",
                "901 mail.com",
                "951 com",
                "50 yahoo.com",
                "1 intel.mail.com",
                "5 wiki.org",
                "5 org",
            ],
        ),  # Example 2
        (
            ["100 a.b.c"],
            ["100 a.b.c", "100 b.c", "100 c"],
        ),  # Single domain with multiple subdomains
        (
            ["1 a.b.c", "1 b.c", "1 c"],
            ["1 a.b.c", "2 b.c", "3 c"],
        ),  # Overlapping subdomains
        (
            ["1000 a.b.c", "2000 b.c", "3000 c"],
            ["1000 a.b.c", "3000 b.c", "6000 c"],
        ),  # Large counts
        ([], []),  # Empty input
        (
            ["1 a.com", "1 b.com", "1 c.com"],
            ["1 a.com", "1 b.com", "1 c.com", "3 com"],
        ),  # Multiple domains with same top-level domain
    ],
)
def test_returns_subdomain_visit_counts(solution, cpdomains, expected):
    assert sorted(solution.subdomainVisits(cpdomains)) == sorted(expected)
