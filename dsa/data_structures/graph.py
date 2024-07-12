from dsa.data_structures import Queue


class GraphMatrix:
    def __init__(self, graph: list[list[int]]) -> None:
        # Each row represents a vertex
        # Each column represents a possible connection
        # The values in the matrix represent edge weights
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
