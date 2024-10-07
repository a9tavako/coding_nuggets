import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if k == 0 or not profits:
            return w

        project = list(zip(capital, profits))
        project.sort()

        current_capital = w
        current_index = 0
        heap = []
        for i in range(k):
            while current_index < len(project) and project[current_index][0] <= current_capital:
                profit = project[current_index][1]
                heapq.heappush(heap, -profit)
                current_index += 1
            
            if not heap:
                return current_capital
            current_capital += -heapq.heappop(heap)
        
        return current_capital