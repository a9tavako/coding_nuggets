from typing import List


def find_max_sum_subarray(nums:List[int]) -> int:
    if not nums:
        raise ValueError(f"Invalid input: {nums}") 

    n = len(nums)
    if n == 1:
        return nums[0]      

    current_sum = 0
    best_no_loop_sum = float("-inf")
    for i in range(n): # time: O(n), space: O(1)
        current_sum += nums[i]
        best_no_loop_sum = max(best_no_loop_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    left_cumul_max_sum = []
    cumul_sum = 0
    best_sum = float("-inf")
    for val in nums:
        cumul_sum += val
        best_sum = max(best_sum, cumul_sum)
        left_cumul_max_sum.append(best_sum)

    right_cumul_max_sum = []
    cumul_sum = 0
    best_sum = float("-inf")
    for i in range(n-1, -1, -1):
        cumul_sum += nums[i]
        best_sum = max(best_sum, cumul_sum)
        right_cumul_max_sum.append(best_sum)
    right_cumul_max_sum.reverse()
    
    best_loop_sum = max(left_cumul_max_sum[i] + right_cumul_max_sum[i+1] for i in range(n-1))

    return max(best_no_loop_sum, best_loop_sum)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        return find_max_sum_subarray(nums)