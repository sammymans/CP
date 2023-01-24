t = int(input())
for _ in range(t):
    n = int(input())
    health = list(map(int,input().split()))
    
    result = 0
    ones = 0
    for h in health:
        if h == 1:
            ones += 1
    
    result = n - ones + ones/2
    if ones % 2 != 0:
        result += 1
    
    print(int(result))
        

