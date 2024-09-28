import pandas as pd
import pytest
from solutions.duplicate_emails import duplicate_emails

@pytest.mark.parametrize("data, expected", [
    (
        pd.DataFrame({"id": [1, 2, 3], "email": ["a@b.com", "c@d.com", "a@b.com"]}),
        pd.DataFrame({"email": ["a@b.com"]})
    ),
    (
        pd.DataFrame({"id": [1, 2, 3, 4], "email": ["a@b.com", "c@d.com", "e@f.com", "g@h.com"]}),
        pd.DataFrame(columns=["email"])
    ),
    (
        pd.DataFrame({"id": [1, 2, 3, 4, 5], "email": ["a@b.com", "a@b.com", "a@b.com", "c@d.com", "c@d.com"]}),
        pd.DataFrame({"email": ["a@b.com", "c@d.com"]})
    ),
    (
        pd.DataFrame({"id": [1], "email": ["a@b.com"]}),
        pd.DataFrame(columns=["email"])
    ),
    (
        pd.DataFrame({"id": [], "email": []}),
        pd.DataFrame(columns=["email"])
    ),
])
def test_duplicate_emails_various_cases(data, expected):
    result = duplicate_emails(data)
    assert result.equals(expected)