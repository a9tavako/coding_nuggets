from typing import List, Set

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []

        if n == 1:
            return [[1]]
        
        if k == 1:
            return [[i] for i in range(1, n+1)]

        if k == 2:
            ans = []
            for i in range(1, n+1):
                for j in range(i+1, n+1):
                    ans.append([i,j])
            return ans

        if k == n:
            return [[i for i in range(1, n+1)]]

        return self.combine(n-1, k) +  [combination + [n] for combination in self.combine(n-1, k-1)]
        