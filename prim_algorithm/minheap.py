import numpy as np
import heapq


class Heap(object):

    def __init__(self):
        """ create a new min-heap. """
        self._heap = []

    def push(self, priority, item):
        """ Push an item with priority into the heap.
            Priority 0 is the highest, which means that such an item will
            be popped first."""
        assert priority >= 0
        heapq.heappush(self._heap, [priority, item])

    def pop(self):
        """ Returns the item with lowest priority. """
        item = heapq.heappop(self._heap)[1] # (prio, item)[1] == item
        return item

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        """ Get all elements ordered by asc. priority. """
        return self

    def next(self):
        """ Get all elements ordered by their priority (lowest first). """
        try:
            return self.pop()
        except IndexError:
            raise StopIteration

    def isInHeap(self, item):
        for i in range(len(self._heap)):
            if self._heap[i][1] == item:
                return True
        return False


    def buildMinHeap(self, items, keys):
        for i in range(len(items)):
            self.push(keys[i], items[i])

    def heapify(self):
        heapq.heapify(self._heap)

    def changeKey(self, item, key):
        for i in range(len(self._heap)):
            if self._heap[i][1] == item:
                self._heap[i][0] = key
        self.heapify()

# test
"""
h = Heap()

key = np.empty(6)
key.fill(np.inf)
p = np.arange(6)

h.buildMinHeap(p, key)
h.changeKey(1,10)
h.changeKey(4,4)
print h._heap
h.heapify()
print h._heap
print h.isInHeap(1)
h.pop()
print h.isInHeap(1)


for item in h:
   print item
"""
