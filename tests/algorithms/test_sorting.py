# tests/test_sorting.py

import pytest
from dsa import bubble_sort, quick_sort


@pytest.fixture
def test_cases():
    return [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]


def test_bubble_sort(test_cases):
    for unsorted, expected in test_cases:
        nums = unsorted[:]
        bubble_sort(nums)
        assert nums == expected


def test_quick_sort(test_cases):
    for unsorted, expected in test_cases:
        nums = unsorted[:]
        quick_sort(nums)
        assert nums == expected
