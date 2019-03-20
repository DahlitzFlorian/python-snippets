import time
import heapq


class PriorityQueue:
    def __init__(self):
        self._q = []

    def add(self, value, priority=0):
        heapq.heappush(self._q, (priority, time.time(), value))

    def pop(self):
        return heapq.heappop(self._q)[-1]


f1 = lambda: print("hello")
f2 = lambda: print("world")

pq = PriorityQueue()
pq.add(f2, priority=1)
pq.add(f1, priority=0)

print(pq.pop()())
print(pq.pop()())
