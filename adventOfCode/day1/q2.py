import sys
from collections import defaultdict

list1, store = [], defaultdict(lambda: 0)

for x in sys.stdin:
    a, b = x.split()
    list1.append(int(a))
    store[int(b)] += 1

score = 0
for x in list1:
    score += x * store[x]
print(score)
