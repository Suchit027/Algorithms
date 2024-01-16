import collections

nums = [5,9,2,-9,-9,-7,-8,7,-9,10]
count = collections.defaultdict(lambda: 0)
for i in nums:
    count[i] += 1
ans = []
for i in nums:
    mul = 1
    for key, value in count.items():
        if i != key:
            mul *= key * value
        else:
            if value > 1:
                value -= 1
                mul *= key * (value)
    ans.append(mul)

print(ans)
