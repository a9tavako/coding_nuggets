#!/bin/python3

import heapq
import os
from typing import List


def get_root(
        node: int,
        parents: List[int]
) -> int:
    current = node
    while current != parents[current]:
        current = parents[current]
    root = current
    current = node
    while parents[current] != root:
        up = parents[current]
        parents[current] = root
        current = up
    return root


def union(
        node1: int,
        node2: int,
        parents: List[int],
        ranks: List[int]
):
    root1 = get_root(node1, parents)
    root2 = get_root(node2, parents)
    if root1 == root2:
        return
    rank_root_1 = ranks[root1]
    rank_root_2 = ranks[root2]
    if rank_root_1 > rank_root_2:
        parents[root2] = root1
        get_root(node2, parents)
        return

    if rank_root_1 == rank_root_2:
        ranks[root2] += 1
    parents[root1] = root2
    get_root(node1, parents)


# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].


def kruskals(
        g_nodes: int,
        g_from: List[int],
        g_to: List[int],
        g_weight: List[int]
) -> int:
    print("inside our function")
    n: int = g_nodes
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    queue = []
    for i in range(len(g_from)):
        start = g_from[i]
        end = g_to[i]
        weight = g_weight[i]
        tie_breaker = start + end
        heapq.heappush(queue, (weight, tie_breaker, start, end))

    edge_count = 0
    graph_weight = 0
    while edge_count < n - 1:
        c_edge = heapq.heappop(queue)
        weight, tie_breaker, start, end = c_edge
        if get_root(start, parents) == get_root(end, parents):
            continue
        union(start, end, parents, ranks)
        edge_count += 1
        graph_weight += weight

    return graph_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')

    fptr.close()
