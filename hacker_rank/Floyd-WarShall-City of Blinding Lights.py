#!/bin/python3

import math
import os
import random
import re
import sys



def pre_calculate_optimal_costs(
    num_nodes,
    road_from, 
    road_to, 
    road_weight
):
    if not road_from:
        raise ValueError(f"Invalid input: {road_from}")
    
    n = num_nodes
    num_edges = len(road_from)
    
    costs = [[float("inf")] * (n+1) for i in range(n+1)]  # 1-indexed
    adj = [set() for i in range(n+1)]
    
    for i in range(num_edges):
        start, end, weight = road_from[i], road_to[i], road_weight[i]
        costs[start][end] = weight
        adj[start].add(end)

    for i in range(1, n+1):
        costs[i][i] = 0
        adj[i].add(i)

    for middle in range(1, n+1):
        for start in range(1, n+1):
            if costs[start][middle] == float("inf"):
                continue
            for end in range(1, n+1):
                costs[start][end] = min(
                    costs[start][end],
                    costs[start][middle] + costs[middle][end]
                )
                
    return costs

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    costs = pre_calculate_optimal_costs(
        road_nodes,
        road_from,
        road_to,
        road_weight
    )

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        
        cost = costs[x][y] if costs[x][y] != float("inf") else -1
        
        print(cost)
