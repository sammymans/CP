t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even, odd = 0, 0
    e, o = [], []
    for i in range(len(a)):
        num = a[i]
        if num % 2:
            odd += 1
            o.append(i + 1)
        else:
            even += 1
            e.append(i + 1)
    
    result = []
    if even >= 2 and odd >= 1:
        print("YES")
        result.append(e.pop())
        result.append(e.pop())
        result.append(o.pop())
        for num in result:
            print(num, end=" ")
    elif odd >= 3:
        print("YES")
        result.append(o.pop())
        result.append(o.pop())
        result.append(o.pop())
        for num in result:
            print(num, end=" ")
    else:
        print("NO")