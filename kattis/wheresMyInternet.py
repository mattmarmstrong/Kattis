# December 2nd, 2021
# Matthew Armstrong

import sys

# Approach -> Treat input as undirected graph, search for cycles using disjoint set operations
# Disjoint set data structure

class DJS:
    # Init
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.sizes = [1] * n

    # Find
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            xp = self.find(self.parent[x])
            self.parent[x] = xp
            return xp

    # Union
    def union(self, x, y):
        xSet = self.find(x)
        ySet = self.find(y)
        if xSet == ySet:
            return

        # Determine which element goes where according to rank
        if self.rank[xSet] < self.rank[ySet]:
            self.parent[xSet] = ySet
            self.sizes[ySet] += self.sizes[xSet]

        elif self.rank[xSet] > self.rank[ySet]:
            self.parent[ySet] = xSet
            self.sizes[xSet] += self.sizes[ySet]

        else:
            self.parent[ySet] = xSet
            self.rank[xSet] += 1
            self.sizes[xSet] += self.sizes[ySet]

    # Check size of x
    def size(self, x):
        return self.sizes[self.find(x)]


numHouses, numNetworks = map(int, sys.stdin.readline().strip().split(" "))

houseSet = DJS(numHouses)

for n in range(numNetworks):
    a, b = map(int, sys.stdin.readline().strip().split(" "))

    a -= 1
    b -= 1

    # print(houseSet.parent, houseSet.rank, houseSet.sizes)
    houseSet.union(a, b)
    # print(houseSet.parent, houseSet.rank, houseSet.sizes)


if houseSet.size(0) == numHouses:
    print("Connected")

else:
    x = houseSet.find(0)
    for i in range(numHouses):
        if houseSet.find(i) != x:
            print(i + 1)



