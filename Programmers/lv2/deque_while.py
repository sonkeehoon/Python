from collections import deque
import time

q = deque()
q.append(10)
q.append(11)
q.appendleft(12)
while q:
    print(q.pop())
    print("empty")
    time.sleep(2)