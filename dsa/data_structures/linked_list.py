class Node[T]:
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: Node[T] | None = None


class LinkedList[T]:
    def __init__(self) -> None:
        self.count = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def append(self, val: T) -> None:
        self.count += 1

        node = Node(val)

        if not self.head or not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def get(self, idx: int) -> T | None:
        if not self.head:
            return

        if idx > self.count - 1 or idx < 0:
            return

        cur = self.head

        for _ in range(idx):
            if cur:
                cur = cur.next

        assert cur is not None

        return cur.val

    def insert_at(self, val: T, idx: int) -> None:
        if idx <= 0:
            return self.prepend(val)

        if idx >= self.count - 1:
            return self.append(val)

        node = Node(val)

        if not self.head:
            self.head = self.tail = node
            return

        cur = self.head

        for _ in range(idx - 1):
            if cur:
                cur = cur.next

        assert cur is not None

        self.count += 1

        node.next = cur.next
        cur.next = node

    def prepend(self, val: T) -> None:
        self.count += 1

        node = Node(val)

        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head = node

    def remove_first(self) -> T | None:
        if not self.head:
            return

        self.count -= 1

        head = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return head.val

    def remove_last(self) -> T | None:
        if not self.head or not self.tail:
            return

        if self.head == self.tail:
            self.count -= 1
            head = self.head
            self.head = self.tail = None
            return head.val

        cur = self.head

        while cur and cur.next != self.tail:
            cur = cur.next

        assert cur is not None

        self.count -= 1

        tail = self.tail
        self.tail = cur
        self.tail.next = None
        return tail.val

    def remove(self, val: T) -> T | None:
        if not self.head:
            return
        if self.head.val == val:
            return self.remove_first()

        cur = self.head

        while cur.next:
            if cur.next.val == val:
                self.count -= 1
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
                return val

            cur = cur.next

    def remove_at(self, idx: int) -> T | None:
        if idx < 0:
            return
        if idx == 0:
            return self.remove_first()
        if idx == self.count - 1:
            return self.remove_last()
        if idx > self.count - 1:
            return

        if not self.head:
            return

        cur = self.head

        for _ in range(idx - 1):
            if cur:
                cur = cur.next

        assert cur is not None and cur.next is not None

        self.count -= 1

        temp = cur.next
        cur.next = cur.next.next

        return temp.val

    def reverse(self) -> None:
        prev = None
        cur = self.head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        self.head = prev

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
