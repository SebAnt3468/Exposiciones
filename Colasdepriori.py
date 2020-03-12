customers = []
customers.append((2, "Harry"))
customers.append((3, "Charles"))
customers.sort(reverse=True)
customers.append((1, "z"))
customers.sort(reverse=True)
customers.append((1, "stacy"))
customers.sort(reverse=False)
print(customers)

import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
    print(heapq.heappop(customers))
