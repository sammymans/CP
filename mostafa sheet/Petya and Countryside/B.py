# find section to pour rain to optimize number of watered sections
# iterate through each index of the heights array, keep spanning outwards with left and right pointers

n = input()
heights = list(map(int,input().split()))

# n = 5
# heights = [1,2,1,2,1]

result = 0

for i in range(len(heights)):
    curr = 1
    left, right = i - 1, i + 1
    # go left
    while left >= 0 and heights[left] <= heights[left + 1]:
        curr += 1
        left -= 1
    # go right
    while right < len(heights) and heights[right] <= heights[right - 1]:
        curr += 1
        right += 1
    result = max(result, curr)

print(result)
    


