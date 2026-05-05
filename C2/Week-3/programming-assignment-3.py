from heapq import heappush, heappop # importing the necessary functions 

hlow = [] # max-heap (smaller half)
hhi = [] # min-heap (larger half)
medians = []

with open('Median.txt') as f:
    for line in f:
        n=int(line.strip()) if line.strip() else None
        if n is None:
            continue
        
        if not hhi or n <= hhi[0]:
            heappush(hlow, -n)
        else:
            heappush(hhi, n)
        
        if len(hlow) > len(hhi) + 1:
            heappush(hhi, -heappop(hlow))
        elif len(hlow) < len(hhi):
            heappush(hlow, -heappop(hhi))
        
        medians.append((-hlow[0]))

print(sum(medians) % 10000)
