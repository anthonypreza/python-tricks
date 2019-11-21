from queue import PriorityQueue
import heapq
from collections import deque
from queue import LifoQueue, Queue
from multiprocessing import Queue as MPQueue
# list is a stack in python
# collections.deque is a linked list based stack implementation

s = []
s.append('eat')
s.append('sleep')
s.append('code')
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())

# deque
# double-ended queue that supports adding and removing elements from either end (queue OR stack)
# implemented as a doubly-linked list
d = deque()
d.append('eat')
d.append('sleep')
d.append('code')
print(d)
print(d.pop())
print(d.pop())
print(d.pop())
# print(d.pop())

# last-in, first-out (lifo) queue
# locking semantics to support multiple concurrent producers and consumers
l = LifoQueue()
l.put('eat')
l.put('sleep')
l.put('code')
print(l)
print(l.get())
print(l.get())
print(l.get())
# print(l.get_nowait())
# print(l.get())

# queues (FIFOs)
# fast first-in, first-out semantics for inserts and deletes
# adding items at back is enqueuing
# removing items at front is dequeuing
# built-in list is a terribly slow queue
q = []
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
print(q.pop(0))  # this is REALLY slow

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())

q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
print(q)
print(q.get())
print(q.get())
print(q.get())
# print(q.get_nowait())

# shared job queues
q = MPQueue()
q.put('eat')
q.put('sleep')
q.put('code')
print(q)
print(q.get())
print(q.get())
print(q.get())

# priority queue
q = []

q.append((2, 'code'))
q.append((1, 'eat'))
q.append((3, 'sleep'))
q.sort(reverse=True)

next_item = q.pop()
print(next_item)

# heapq - binary heap implementation
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

next_item = heapq.heappop(q)
print(next_item)


q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

next_item = q.get()
print(next_item)
