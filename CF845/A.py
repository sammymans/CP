t = int(input())
result = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    curr = 0
    if n != 1:

        i, j = 0, 1

        while j < n:
            if a[i] % 2 == 0 and a[j] % 2 == 0 or a[i] % 2 != 0 and a[j] % 2 != 0:
                curr += 1
            i += 1
            j += 1
        
    result.append(curr)
    
for num in result:
    print(num)