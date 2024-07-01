import pytest
from dsa import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def sample_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    return ll


def test_init(empty_list):
    assert empty_list.count == 0
    assert empty_list.head is None
    assert empty_list.tail is None


def test_append(empty_list):
    empty_list.append(1)
    assert empty_list.count == 1
    assert empty_list.head.val == 1
    assert empty_list.tail.val == 1

    empty_list.append(2)
    assert empty_list.count == 2
    assert empty_list.head.val == 1
    assert empty_list.tail.val == 2


def test_get(sample_list):
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 2
    assert sample_list.get(2) == 3
    assert sample_list.get(3) is None
    assert sample_list.get(-1) is None


def test_insert_at_middle(sample_list):
    sample_list.insert_at(4, 1)
    assert sample_list.count == 4
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 4
    assert sample_list.get(2) == 2
    assert sample_list.get(3) == 3


def test_insert_at_beginning(sample_list):
    sample_list.insert_at(0, 0)
    assert sample_list.count == 4
    assert sample_list.get(0) == 0
    assert sample_list.get(1) == 1


def test_insert_at_end(sample_list):
    sample_list.insert_at(4, 3)
    assert sample_list.count == 4
    assert sample_list.get(3) == 4


def test_prepend(sample_list):
    sample_list.prepend(0)
    assert sample_list.count == 4
    assert sample_list.get(0) == 0
    assert sample_list.get(1) == 1


def test_remove_first(sample_list):
    assert sample_list.remove_first() == 1
    assert sample_list.count == 2
    assert sample_list.get(0) == 2


def test_remove_first_last_element():
    ll = LinkedList()
    ll.append(1)
    assert ll.remove_first() == 1
    assert ll.count == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_first_empty_list(empty_list):
    assert empty_list.remove_first() is None


def test_remove_last(sample_list):
    assert sample_list.remove_last() == 3
    assert sample_list.count == 2
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 2


def test_remove_last_single_element():
    ll = LinkedList()
    ll.append(1)
    assert ll.remove_last() == 1
    assert ll.count == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_last_empty_list(empty_list):
    assert empty_list.remove_last() is None


def test_remove_existing(sample_list):
    assert sample_list.remove(2) == 2
    assert sample_list.count == 2
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 3


def test_remove_non_existing(sample_list):
    assert sample_list.remove(4) is None
    assert sample_list.count == 3


def test_remove_at_middle(sample_list):
    assert sample_list.remove_at(1) == 2
    assert sample_list.count == 2
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 3


def test_remove_at_beginning(sample_list):
    assert sample_list.remove_at(0) == 1
    assert sample_list.count == 2
    assert sample_list.get(0) == 2


def test_remove_at_end(sample_list):
    assert sample_list.remove_at(2) == 3
    assert sample_list.count == 2
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 2


def test_remove_at_invalid_index(sample_list):
    assert sample_list.remove_at(3) is None
    assert sample_list.count == 3


def test_reverse(sample_list):
    sample_list.reverse()
    assert sample_list.count == 3
    assert sample_list.get(0) == 3
    assert sample_list.get(1) == 2
    assert sample_list.get(2) == 1


def verify_list_state(ll: LinkedList, expected_values: list[int]):
    assert ll.count == len(expected_values)
    for i, value in enumerate(expected_values):
        assert ll.get(i) == value
    assert ll.get(len(expected_values)) is None
    if expected_values:
        assert ll.tail and ll.tail.val == expected_values[-1]
    else:
        assert ll.tail is None


def test_count_accuracy():
    ll = LinkedList()
    verify_list_state(ll, [])

    ll.append(1)
    verify_list_state(ll, [1])

    ll.append(2)
    verify_list_state(ll, [1, 2])

    ll.prepend(0)
    verify_list_state(ll, [0, 1, 2])

    ll.remove_first()
    verify_list_state(ll, [1, 2])

    ll.remove_last()
    verify_list_state(ll, [1])

    ll.insert_at(3, 1)
    verify_list_state(ll, [1, 3])

    ll.remove(3)
    verify_list_state(ll, [1])

    ll.remove_at(0)
    verify_list_state(ll, [])
