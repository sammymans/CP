from collections import defaultdict

s = input()
t = input()

# s = "zzzZZZ"
# t = "ZZZzzZ"

have = defaultdict(int)
for c in t:
    have[c] = have.get(c, 0) + 1

yays, whoops = 0, 0
for c in s:
    if have[c] > 0:
        yays += 1
        have[c] -= 1

for c in s:
    if c.islower(): opp = c.upper()
    else: opp = c.lower()

    if have[opp] > 0:
        whoops += 1
        have[opp] -= 1

print(yays, whoops)
