class Node[T]:
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: Node[T] | None = None


class Queue[T]:
    def __init__(self) -> None:
        self.count = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def enqueue(self, val: T) -> None:
        self.count += 1

        node = Node(val)

        if not self.head or not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def deque(self) -> T | None:
        if not self.head:
            return

        self.count -= 1

        head = self.head

        self.head = self.head.next

        if not self.head:
            self.tail = None

        return head.val

    def peek(self) -> T | None:
        return self.head.val if self.head else None

    def __repr__(self) -> str:
        res = ""
        cur = self.head

        while cur:
            if cur.next:
                res += f"{cur.val} -> "
            else:
                res += f"{cur.val}"

            cur = cur.next

        return res
