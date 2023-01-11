first = list(map(int, input().split()))
n, a = first[0], first[1]-1
cities = list(map(int, input().split()))

left, right = a-1, a+1
result = 0

if cities[a] == 1:
    result += 1

while left >= 0 and right < n:
    if cities[left] == 1 and cities[right] == 1:
        result += 2
    left -= 1
    right += 1

if left == -1 and right < n:
    for num in cities[right:]:
        result += num
elif right == n :
    for num in cities[:left+1]:
        result += num

print(result)

