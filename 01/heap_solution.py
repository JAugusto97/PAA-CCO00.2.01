# Caio Ueno e João Augusto Leite

from typing import List


class MinHeap:

    """
    MinHeap data structure.
    """

    def __init__(self):
        self.heap = []
        self.size = 0

    @property
    def root(self):
        if self.size > 0:
            return self.heap[0]
        else:
            return -1

    @staticmethod
    def parent(idx: int):
        return idx // 2

    @staticmethod
    def left(idx: int):
        return 2 * idx + 1

    @staticmethod
    def right(idx: int):
        return 2 * idx + 2

    def heap_insert(self, elem: float):
        """Insert an element normally (last index and then fix its position)."""
        self.heap.append(elem)
        self.size += 1  # increase before calling bubble up
        self.bubble_up()

    def root_insert(self, elem: float):
        """Insert an element on the root, and then fix its position."""
        self.heap[0] = elem
        self.bubble_down()

    def swap(self, idx_a: int, idx_b: int):
        """Swap two elements in the heap."""
        tmp = self.heap[idx_a]
        self.heap[idx_a] = self.heap[idx_b]
        self.heap[idx_b] = tmp

    def bubble_down(self):
        """Fix position of root element."""
        idx = 0
        while idx < self.size:

            # no children
            if MinHeap.left(idx) > self.size - 1:
                break

            # no right children
            elif MinHeap.right(idx) > self.size - 1:
                # right position
                if self.heap[idx] < self.heap[MinHeap.left(idx)]:
                    break
                else:
                    self.swap(idx, MinHeap.left(idx))
                    idx = MinHeap.left(idx)

            # both children
            else:
                # right position
                if (
                    self.heap[idx] < self.heap[MinHeap.left(idx)]
                    and self.heap[idx] < self.heap[MinHeap.right(idx)]
                ):
                    break

                # select min child to swap
                if self.heap[MinHeap.left(idx)] > self.heap[MinHeap.right(idx)]:
                    self.swap(idx, MinHeap.right(idx))
                    idx = MinHeap.right(idx)
                else:
                    self.swap(idx, MinHeap.left(idx))
                    idx = MinHeap.left(idx)

    def bubble_up(self):
        """Fix position of last element."""
        idx = self.size - 1
        while idx > 0 and self.heap[idx] < self.heap[self.parent(idx)]:
            self.swap(idx, self.parent(idx))
            idx = self.parent(idx)


def kth_highest_elem(k: int, arr: List[float]):

    """Return the k-th highest element in the given list."""

    heap = MinHeap()

    for i, elem in enumerate(arr):
        if i < k:
            heap.heap_insert(elem=elem)
        else:
            # if heap root is greater than elem
            # then don't insert it
            if elem > heap.root:
                heap.root_insert(elem=elem)

    return heap.root


if __name__ == "__main__":
    
    N = int(input())
    for _ in range(N):
        # read line
        user_input_list = input().split()

        K = int(user_input_list[0])        
        scores_sorted = kth_highest_elem(
            K, [float(score) for score in user_input_list[2:]]
        )
        # output
        print(format(scores_sorted, ".2f"))
