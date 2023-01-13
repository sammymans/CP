n = int(input())
# n = 5
a, b, c = [], [], [0] * n

if n % 2 == 0:
    print(-1)
else:
    for i in range(n):
        a.append(i)
    for i in range(n):
        b.append((i + 1)%n)
    for i in range(n):
        c[i] = (a[i] + b[i]) % n
        
    for i in range(n):
        print(a[i], end=" ")
    print()
    for i in range(n):
        print(b[i], end=" ")
    print()
    for i in range(n):
        print(c[i], end=" ")



    
