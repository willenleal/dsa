from dsa.data_structures import Queue


class GraphMatrix:
    def __init__(self, graph: list[list[int]]) -> None:
        self.graph = graph

    def bfs(self, source: int, target: int) -> None | list[int]:
        seen = [False] * len(self.graph)
        prev = [-1] * len(self.graph)

        q = Queue[int]()

        seen[source] = True
        q.enqueue(source)

        while len(q):
            cur = q.deque()

            if cur is None:
                break

            if cur == target:
                path = []

                while cur != -1:
                    path.append(cur)
                    cur = prev[cur]

                return path[::-1]

            for i, weight in enumerate(self.graph[cur]):
                if weight == 0 or seen[i]:
                    continue

                seen[i] = True
                prev[i] = cur
                q.enqueue(i)

        return None


class GraphList:
    def __init__(self, graph: list[list[dict[str, int]]]) -> None:
        self.graph = graph

    def dfs(self, source: int, target: int) -> list[int] | None:
        seen = [False] * len(self.graph)
        path: list[int] = []

        self._dfs(source, target, seen, path)

        if len(path) == 0:
            return None

        return path

    def _dfs(self, cur: int, target: int, seen: list[bool], path: list[int]) -> bool:
        if seen[cur]:
            return False

        seen[cur] = True

        path.append(cur)
        if cur == target:
            return True

        for edge in self.graph[cur]:
            if "to" in edge and self._dfs(edge["to"], target, seen, path):
                return True

        path.pop()

        return False
