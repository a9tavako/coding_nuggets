class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [gas[i] - cost[i] for i in range(len(gas))]

        diffs = diffs + diffs # we duplicate the diffs to account for the circular pattern
        start = 0
        c_sum = 0
        c_start = 0
        best_sum = 0
        best_start = 0
        for i in range(len(diffs)):
            c_sum += diffs[i]

            if c_sum > best_sum:
                best_sum = c_sum
                best_start = c_start

            if c_sum < 0:
                c_sum = 0
                c_start = i + 1

        if best_sum < 0:
            return -1

        cum_sum = 0
        for i in range(best_start, best_start + len(gas)):
            cum_sum += diffs[i]
            if cum_sum < 0:
                return -1
        
        return best_start