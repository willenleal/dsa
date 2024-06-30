from dsa import Queue


def test_queue_initialization():
    queue = Queue[int]()
    assert queue.count == 0


def test_queue_enqueue():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.count == 3
    assert queue.peek() == 1


def test_queue_deque():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.deque() == 1
    assert queue.count == 2
    assert queue.deque() == 2
    assert queue.count == 1
    assert queue.deque() == 3
    assert queue.count == 0
    assert queue.deque() is None


def test_queue_peek():
    queue = Queue[int]()
    assert queue.peek() is None
    queue.enqueue(1)
    assert queue.peek() == 1
    queue.enqueue(2)
    assert queue.peek() == 1
    queue.deque()
    assert queue.peek() == 2


def test_queue_count_consistency():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.deque()
    queue.enqueue(3)
    assert queue.count == 2
    queue.deque()
    queue.deque()
    assert queue.count == 0
    queue.deque()
    queue.deque()
    assert queue.count == 0
