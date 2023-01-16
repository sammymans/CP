from collections import deque
import math

n = int(input())
k1, *p1 = input().split()
p1 = list(map(int, p1))

k2, *p2 = input().split()
p2 = list(map(int, p2))

# n = 4
# k1, p1 = 2, [1,3]
# k2, p2 = 2, [4,2]

p1, p2 = deque(p1), deque(p2)
visited = set()
count = 0

loop = False

while p1 and p2:
    p_first, p_second = p1.popleft(), p2.popleft()

    # math.factorial(n)
    if count > 110:
        loop = True
        break

    if p_first > p_second:
        p1.append(p_second)
        p1.append(p_first)
    else:
        p2.append(p_first)
        p2.append(p_second)
    
    count += 1
    visited.add((p_first, p_second))

if loop:
    print(-1)
elif p1 and not p2:
    print(count, end=" ")
    print(1)
elif p2 and not p1:
    print(count, end=" ")
    print(2)