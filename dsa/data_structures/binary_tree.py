from typing import override

from dsa.data_structures import Queue


class Node[T: (int, float)]:
    def __init__(self, val: T) -> None:
        self.val = val
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None


class BT[T: (int, float)]:
    def __init__(self) -> None:
        self.root: Node[T] | None = None
        self.size = 0

    @property
    def height(self):
        if not self.root:
            return -1
        return self._height(self.root)

    def _height(self, node: Node[T] | None) -> int:
        if node is None:
            return 0

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return max(left_height, right_height) + 1

    def insert(self, val: T) -> None:
        self.size += 1

        if not self.root:
            self.root = Node(val)
            return

        q = Queue[Node[T] | None]()
        q.enqueue(self.root)

        while len(q):
            cur = q.deque()

            if not cur:
                break

            if not cur.left:
                cur.left = Node(val)
                break
            else:
                q.enqueue(cur.left)

            if not cur.right:
                cur.right = Node(val)
                break

            else:
                q.enqueue(cur.right)

    def dfs(self, val: T) -> bool:
        return self._dfs(self.root, val)

    def _dfs(self, node: Node[T] | None, val: T) -> bool:
        if not node:
            return False

        if node.val == val:
            return True

        return self._dfs(node.left, val) or self._dfs(node.right, val)

    def bfs(self, val: T) -> bool:
        q = Queue[Node[T] | None]()

        q.enqueue(self.root)

        while len(q):
            cur = q.deque()

            if not cur:
                continue

            if cur.val == val:
                return True

            q.enqueue(cur.left)
            q.enqueue(cur.right)

        return False

    def invert(self) -> None:
        return self._invert(self.root)

    def _invert(self, node: Node[T] | None) -> None:
        if not node:
            return

        node.right, node.left = node.left, node.right

        if node.left:
            self._invert(node.left)
        if node.right:
            self._invert(node.right)

    def _eq(self, a: Node[T] | None, b: Node[T] | None) -> bool:
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return self._eq(a.left, b.left) and self._eq(a.right, b.right)

    def __eq__(self, bst: object) -> bool:
        if not isinstance(bst, BT):
            return NotImplemented
        return self._eq(self.root, bst.root)

    def __repr__(self) -> str:
        return self._repr(self.root)

    def _repr(self, node: Node[T] | None, level: int = 0) -> str:
        if not node:
            return ""

        left = self._repr(node.left, level + 1)
        cur = f"{' ' * 4 * level} {"->" if level > 0 else "*"} {node.val}\n"
        right = self._repr(node.right, level + 1)

        return f"{right}{cur}{left}"


class BST[T: (int, float)](BT[T]):
    @override
    def insert(self, val: T) -> None:
        self.size += 1
        if not self.root:
            self.root = Node(val)
            return

        return self._insert(self.root, val)

    def _insert(self, node: Node[T], val: T) -> None:
        if val > node.val:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)
        else:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)

    @override
    def dfs(self, val: T) -> bool:
        return self._dfs(self.root, val)

    @override
    def _dfs(self, node: Node[T] | None, val: T) -> bool:
        if not node:
            return False

        if val == node.val:
            return True

        if val < node.val:
            return self._dfs(node.left, val)
        else:
            return self._dfs(node.right, val)

    def deleteNode(self, val: T) -> bool:
        _, res = self._deleteNode(self.root, val)
        if res:
            self.size -= 1
        return res

    def _deleteNode(self, node: Node[T] | None, val: T) -> tuple[Node[T] | None, bool]:
        if not node:
            return node, False

        elif val < node.val:
            node.left, res = self._deleteNode(node.left, val)
        elif val > node.val:
            node.right, res = self._deleteNode(node.right, val)
        else:
            if not node.left:
                return node.right, True
            if not node.right:
                return node.left, True

            cur = node.left

            while cur.right:
                cur = cur.right

            node.val = cur.val
            node.left, _ = self._deleteNode(node.left, node.val)
            return node, True

        return node, res
