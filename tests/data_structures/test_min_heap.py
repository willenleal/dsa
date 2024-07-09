import pytest
from dsa import MinHeap


@pytest.fixture
def min_heap():
    return MinHeap[int]()


def test_insert(min_heap):
    min_heap.insert(5)
    assert len(min_heap) == 1
    assert min_heap.data[0] == 5

    min_heap.insert(3)
    assert len(min_heap) == 2
    assert min_heap.data[0] == 3
    assert min_heap.data[1] == 5

    min_heap.insert(8)
    assert len(min_heap) == 3
    assert min_heap.data[0] == 3
    assert min_heap.data[1] == 5
    assert min_heap.data[2] == 8


def test_pop(min_heap):
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)

    assert min_heap.pop() == 3
    assert len(min_heap) == 2

    assert min_heap.pop() == 5
    assert len(min_heap) == 1

    assert min_heap.pop() == 8
    assert len(min_heap) == 0

    assert min_heap.pop() is None


def test_len(min_heap):
    assert len(min_heap) == 0
    min_heap.insert(5)
    assert len(min_heap) == 1
    min_heap.insert(3)
    assert len(min_heap) == 2
    min_heap.pop()
    assert len(min_heap) == 1
    min_heap.pop()
    assert len(min_heap) == 0
