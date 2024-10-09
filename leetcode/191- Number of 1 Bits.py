class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        current = n
        for _ in range(32):
            if 1 & current == 1:
                count += 1
            current = current >> 1
        
        return count