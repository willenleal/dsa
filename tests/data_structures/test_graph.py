import pytest

from dsa.data_structures.graph import GraphMatrix


@pytest.fixture
def graph():

    #     >(1)<--->(4) ---->(5)
    #    /          |       /|
    # (0)     ------|------- |
    #    \   v      v        v
    #     >(2) --> (3) <----(6)
    weighed_adjacent_matrix = [
        [0, 3, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 5, 0, 2, 0],
        [0, 0, 18, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1],
    ]
    return GraphMatrix(weighed_adjacent_matrix)


def test_bfs(graph):
    assert graph.bfs(0, 6) == [0, 1, 4, 5, 6]
    assert graph.bfs(0, 3) == [0, 1, 4, 3]
    assert graph.bfs(2, 5) is None
    assert graph.bfs(6, 0) is None
