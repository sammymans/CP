from heapq import heappush, heappop

ins = list(map(int,input().split()))
n = ins[0]
k = ins[1]
cards = input()

# print(n, k, cards)

count = {}

for c in cards:
    count[c] = count.get(c, 0) + 1

maxHeap = []
for val in count.values():
    heappush(maxHeap, -1* val)

result = 0

while maxHeap and k > 0:
    highest = heappop(maxHeap) * -1
    if highest >= k:
        result += k**2
        break
    else:
        result += highest**2
        k -= highest

print(result)



