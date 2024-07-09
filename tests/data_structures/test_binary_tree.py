from dsa import BT, BST


def test_bt_insert():
    bt = BT[int]()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    assert bt.size == 3


def test_bt_height():
    bt = BT[int]()
    assert bt.height is -1
    bt.insert(1)
    assert bt.height == 1
    bt.insert(2)
    bt.insert(3)
    assert bt.height == 2


def test_bt_dfs():
    bt = BT[int]()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    assert bt.dfs(2) is True
    assert bt.dfs(4) is False


def test_bt_bfs():
    bt = BT[int]()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    assert bt.bfs(2) is True
    assert bt.bfs(4) is False


def test_bt_invert():
    bt1 = BT[int]()
    bt1.insert(1)
    bt1.insert(2)
    bt1.insert(3)

    bt2 = BT[int]()
    bt2.insert(1)
    bt2.insert(3)
    bt2.insert(2)

    bt1.invert()
    assert bt1 == bt2


def test_bt_equality():
    bt1 = BT[int]()
    bt1.insert(1)
    bt1.insert(2)
    bt1.insert(3)

    bt2 = BT[int]()
    bt2.insert(1)
    bt2.insert(2)
    bt2.insert(3)

    assert bt1 == bt2

    bt2.insert(4)
    assert bt1 != bt2


def test_bst_insert():
    bst = BST[int]()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.size == 3


def test_bst_dfs():
    bst = BST[int]()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    assert bst.dfs(2) is True
    assert bst.dfs(4) is False


def test_bst_delete_node():
    bst = BST[int]()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)

    assert bst.deleteNode(1) is True
    assert bst.dfs(1) is False
    assert bst.size == 2
    assert bst.deleteNode(4) is False
    assert bst.size == 2


def test_bst_delete_root():
    bst = BST[int]()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)

    assert bst.deleteNode(2) is True
    assert bst.root is not None
    assert bst.root.val in (1, 3)
    assert bst.dfs(2) is False
