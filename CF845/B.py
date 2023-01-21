from math import factorial

m = 1000000007
t = int(input())
result = []

for _ in range(t):
    n = int(input())
    if n == 1:
        result.append(0)
    else:
        orderings = n * (n-1)
        result.append((factorial(n) * orderings) % m)

    # print('-->' + str(factorial(n) ** 2))

for num in result:
    print(num)
