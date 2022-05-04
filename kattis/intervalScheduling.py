# December 2nd, 2021
# Matthew Armstrong

import sys

n = int(sys.stdin.readline())

intervals = []

for i in range(n):
    data = sys.stdin.readline().strip().split(" ")
    dataToInt = [int(x) for x in data]
    intervals.append(dataToInt)

intervals.sort(key=lambda x: x[1])


def max_tasks(interval_list):
    #: Assumption: You can always complete at least one task. Hence, n = 1
    tasks = 1

    firstDone = min(interval_list, key=lambda y: y[1])

    for x in range(len(interval_list)):
        current = interval_list[x]
        if firstDone[1] <= current[0]:
            #: you can finish another task
            tasks += 1
            firstDone = current

    return tasks


print(max_tasks(intervals))
