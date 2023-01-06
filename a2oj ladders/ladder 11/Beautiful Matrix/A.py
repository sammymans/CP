ROWS, COLS = 5, 5

for i in range(ROWS):
    row = list(map(int, input().split()))
    for j in range(COLS):
        if row[j] == 1:
            moves = abs(j-2) + abs(i-2)
            print(moves)



# practice inputting the entire matrix

# matrix = []
# i = 0
# while i < 5:
#     row = list(map(int,input().split()))
#     matrix.append(row)
#     i += 1

# print(matrix)