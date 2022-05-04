# December 2nd, 2021
# Matthew Armstrong

import heapq


#implement dijkstra's algorithm 
def dijkstra(adj, start):
    q = [(0, start)]
    dists = dict()
    while q:
        d, u = heapq.heappop(q)
        if u in dists:
            continue
        dists[u] = d
        for v, w