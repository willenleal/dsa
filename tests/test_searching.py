import pytest
from dsa.algorithms.searching import binary_search


@pytest.fixture
def test_cases():
    return [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, False),
        ([], 1, False),
        ([5], 5, True),
        ([5], 1, False),
        ([1, 2, 3, 4, 5], 1, True),
        ([1, 2, 3, 4, 5], 5, True),
    ]


def test_binary_search(test_cases):
    for nums, target, expected in test_cases:
        assert binary_search(nums, target) == expected
