import sys

list1, list2 = [], []

for line in sys.stdin:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

ans = 0

for i in range(len(list1)):
    ans += abs(list1[i] - list2[i])

print(ans)