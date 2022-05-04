# December 2nd, 2021
# Matthew Armstrong

import sys

capacity, n = map(int, sys.stdin.readline().strip().split(" "))

values = []
weights = []

for i in range(n):
    v, w = map(int, sys.stdin.readline().strip().split(" "))

    values.append(v)
    weights.append(w)


# function that builds dynamic programming table
def knapsack(v, w, c, n):
    dp = [[0 for i in range(c + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(c + 1):

            if i == 0 or j == 0:
                dp[i][j] = 0

            elif w[i - 1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j])

            else:
                dp[i][j] = dp[i - 1][j]

    return dp


def which_items(v, w, c, n, dp):
    items = []
    totalValue = dp[n][c]
    weightLeft = c
    while (weightLeft > 0):
        for i in range(n, 0, -1):
            if totalValue == dp[i - 1][c]:
                continue
            else:
                items.append(i)
                totalValue -= v[i - 1]
                weightLeft -= w[i - 1]
        return items


dp = knapsack(values, weights, capacity, n)

itemList = which_items(values, weights, capacity, n, dp)
itemList.reverse()

for i in itemList:
    print(str(i))


for i in itemList:
    print(str(i))
