class Node[T]:
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: None | Node[T] = None


class Stack[T]:
    def __init__(self) -> None:
        self.count = 0
        self.head: Node[T] | None = None

    def push(self, val: T) -> None:
        self.count += 1
        node = Node(val)

        if not self.head:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def pop(self) -> T | None:
        if not self.head:
            return

        self.count -= 1

        head = self.head
        self.head = self.head.next

        return head.val

    def peek(self) -> T | None:
        return self.head.val if self.head else None

    def __len__(self):
        return self.count

    def __repr__(self) -> str:
        res = ""
        cur = self.head

        while cur:
            res += f"{cur.val}\n"
            cur = cur.next

        return res
