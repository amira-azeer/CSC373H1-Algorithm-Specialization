# Two-Sum Algorithm
from collections import defaultdict

with open('algo1-programming_prob-2sum.txt') as f:
    data = f.readlines()

nums = defaultdict(list)
for line in data:
    if num := line.strip():
        n = int(num)
        nums[n // 10000].append(n)

res = set()
for key1, xs in list(nums.items()):
    for key2 in range(-key1 - 2, -key1 + 1):
        for x in xs:
            for y in nums.get(key2, []):
                if abs(x + y) < 10000:
                    res.add(x + y)

print(len(res))
