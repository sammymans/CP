from collections import defaultdict
from math import comb

n = int(input())
points = []
for i in range(n):
    line = list(map(int,input().split()))
    points.append(line)

dict_v, dict_h = defaultdict(list), defaultdict(list)
repeats = defaultdict(int)
visited = set()
for point in points:
    x, y = point[0], point[1]
    dict_v[x].append(point)
    dict_h[y].append(point)
    visited.add((x,y))
    if (x,y) in visited:
        repeats[(x,y)] += 1

result = 0
for key in dict_v:
    vals = dict_v[key]
    result += comb(len(vals),2)

for key in dict_h:
    vals = dict_h[key]
    result += comb(len(vals),2)

repeat = 0
for val in repeats.values():
    repeat += comb(val, 2)

print(result - repeat)

