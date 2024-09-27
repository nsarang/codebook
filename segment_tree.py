class SegmentTree:
    """
    Segment Tree with point updates and range queries

    T[0] is the root
    T[1 : n] are the internal nodes
    T[n : 2n] are the leaves (values)

    Note:
        - (2 * i) and (2 * i + 1) are the left and right children of node i.
        - i // 2 is the parent of node i.
    """
    def __init__(self, values) -> None:
        self.n = n = len(values)
        self.t = [0] * (2 * n + 1)
        for i in range(n):
            self.t[i + n] = values[i]
        for i in reversed(range(1, n)):
            self.t[i] = self.combine(self.t[2 * i], self.t[2 * i + 1])

    def modify(self, p, value):
        """Set the value at index p"""
        p += self.n
        self.t[p] = value
        # Bubble up the change
        while p := p // 2:
            self.t[p] = self.combine(self.t[2 * p], self.t[2 * p + 1])

    def query(self, l, r):  # sum on interval [l, r)
        resl = resr = 0
        # Start from the leaves and move up
        l, r = l + self.n, r + self.n
        while l < r:
            if l & 1:  # l is the right child and its parent is not included
                resl = self.combine(resl, self.t[l])
                l += 1
            if r & 1:
                # r is the right child. Move to its sibling
                r -= 1
                resr = self.combine(self.t[r], resr)
            l, r = l // 2, r // 2
        return self.combine(resl, resr)

    def combine(self, lv, rv):
        raise NotImplementedError


class ST_MAX(SegmentTree):
    def combine(self, lv, rv):
        return max(lv, rv)


if __name__ == "__main__":
    st = ST_MAX([8, 5, 10, 12, -3, 0, 8, 1])
    st.modify(2, -10)
    print(st.query(0, 3))
    print(st.query(2, 5))
    print(st.query(4, 6))
