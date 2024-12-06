import sys

safe = 0

for line in sys.stdin:
    data = line.split()
    if len(data) < 3:
        safe += 1
        continue
    diff = int(data[1]) - int(data[0])
    if not 1 <= abs(diff) <= 3:
        continue
    if diff > 0:
        ascending = True
    elif diff < 0:
        ascending = False
    else:
        continue
    check = True
    for i in range(2, len(data)):
        diff = int(data[i]) - int(data[i - 1])
        if (diff > 0 and not ascending) or (diff < 0 and ascending) or not 1 <= abs(diff) <= 3: 
            check = False
            break
    if check:
        safe += 1

print(safe)