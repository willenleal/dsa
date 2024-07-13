import pytest

from dsa.data_structures.graph import GraphMatrix
from dsa.data_structures.graph import GraphList


@pytest.fixture
def graph_matrix():
    # Each row represents a vertex
    # Each column represents a possible connection
    # The values in the matrix represent edge weights
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


@pytest.fixture
def graph_list1():
    #     >(1)<--->(4) ---->(5)
    #    /          |       /|
    # (0)     ------|------- |
    #    \   v      v        v
    #     >(2) --> (3) <----(6)
    list2 = [[] for _ in range(7)]
    list2[0] = [{"to": 1, "weight": 3}, {"to": 2, "weight": 1}]
    list2[1] = [{"to": 4, "weight": 1}]
    list2[2] = [{"to": 3, "weight": 7}]
    list2[3] = []
    list2[4] = [{"to": 1, "weight": 1}, {"to": 3, "weight": 5}, {"to": 5, "weight": 2}]
    list2[5] = [{"to": 2, "weight": 18}, {"to": 6, "weight": 1}]
    list2[6] = [{"to": 3, "weight": 1}]
    return GraphList(list2)


def test_bfs(graph_matrix):
    assert graph_matrix.bfs(0, 6) == [0, 1, 4, 5, 6]
    assert graph_matrix.bfs(0, 3) == [0, 1, 4, 3]
    assert graph_matrix.bfs(2, 5) is None
    assert graph_matrix.bfs(6, 0) is None


def test_dfs_path_exists(graph_list1):
    assert graph_list1.dfs(6, 0) is None
    assert graph_list1.dfs(0, 6) == [0, 1, 4, 5, 6]
