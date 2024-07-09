class MinHeap[T: (int | float)]:
    def __init__(self) -> None:
        self.count = 0
        self.data: list[T] = []

    def insert(self, val: T) -> None:
        if self.count < len(self.data):
            self.data[self.count] = val
        else:
            self.data.append(val)
        self._heapify_up(self.count)
        self.count += 1

    def pop(self) -> T | None:
        if self.count == 0:
            return

        v = self.data[0]

        self.count -= 1
        if self.count == 0:
            self.data = []
            return v

        self.data[0] = self.data[self.count]
        self._heapify_down(0)
        return v

    def _heapify_down(self, idx: int) -> None:
        lc_idx = self._get_left_child_idx(idx)
        rc_idx = self._get_right_child_idx(idx)

        if idx >= self.count or lc_idx >= self.count:
            return

        lc_v = self.data[lc_idx]
        rc_v = self.data[rc_idx]
        v = self.data[idx]

        if lc_v > rc_v and v > rc_v:
            self.data[rc_idx], self.data[idx] = v, rc_v
            self._heapify_down(rc_idx)
        elif rc_v > lc_v and v > lc_v:
            self.data[lc_idx], self.data[idx] = v, lc_v
            self._heapify_down(lc_idx)

    def _heapify_up(self, idx: int) -> None:
        if idx == 0:
            return

        p = self._get_parent_idx(idx)

        if self.data[p] > self.data[idx]:
            self.data[p], self.data[idx] = self.data[idx], self.data[p]
            self._heapify_up(p)

    def _get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2

    def _get_left_child_idx(self, idx: int) -> int:
        return 2 * idx + 1

    def _get_right_child_idx(self, idx: int) -> int:
        return 2 * idx + 2

    def __len__(self) -> int:
        return self.count

    def __repr__(self) -> str:
        return f"[{",".join(str(v) for v in self.data)}]"
