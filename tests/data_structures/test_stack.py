from dsa import Stack


def test_stack_initialization():
    stack = Stack[int]()
    assert stack.count == 0


def test_stack_push():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.count == 3
    assert stack.peek() == 3


def test_stack_pop():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.count == 2
    assert stack.pop() == 2
    assert stack.count == 1
    assert stack.pop() == 1
    assert stack.count == 0
    assert stack.pop() is None


def test_stack_peek():
    stack = Stack[int]()
    assert stack.peek() is None
    stack.push(1)
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 2
    stack.pop()
    assert stack.peek() == 1


def test_stack_count_consistency():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.push(3)
    assert stack.count == 2
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.count == 0
