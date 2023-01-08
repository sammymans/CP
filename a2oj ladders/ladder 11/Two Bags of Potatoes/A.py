y, k, n = list(map(int, input().split()))

result = []
x = k - y % k

while x + y <= n:
    result.append(x)
    x += k

if result == []:
    print(-1)
else:
    for num in result:
        print(num, end=" ")