import math

def gcd(x,y):
    return math.gcd(x,y)

def lcm(x,y):
    return (x*y) // gcd(x,y)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0] * nums[0]
        
        left_gcd = []
        left_lcm = [] 
        gcd_cumul = nums[0]
        lcm_cumul = nums[0]
        for val in nums:
            gcd_cumul = gcd(gcd_cumul, val)
            left_gcd.append(gcd_cumul)

            lcm_cumul = lcm(lcm_cumul, val)
            left_lcm.append(lcm_cumul)
        
        right_gcd = [0] * len(nums)
        right_lcm = [0] * len(nums)
        gcd_cumul = nums[-1]
        lcm_cumul = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            gcd_cumul = gcd(gcd_cumul, nums[i])
            right_gcd[i] = gcd_cumul

            lcm_cumul = lcm(lcm_cumul, nums[i])
            right_lcm[i] = lcm_cumul

        gcd_minus_one = [0] * len(nums)
        lcm_minus_one = [0] * len(nums)
        for i in range(len(nums)):
            if i > 0 and i < len(nums)-1:
                gcd_minus_one[i] = gcd(left_gcd[i-1], right_gcd[i+1])
                lcm_minus_one[i] = lcm(left_lcm[i-1], right_lcm[i+1])
            elif i == 0:
                gcd_minus_one[i] = right_gcd[i+1]
                lcm_minus_one[i] = right_lcm[i+1]
            elif i == len(nums) - 1:
                gcd_minus_one[i] = left_gcd[i-1]
                lcm_minus_one[i] = left_lcm[i-1]
            else:
                raise ValueError("This shouldn't happen")


        form_factors = [0] * len(nums)
        for i in range(len(nums)):
            form_factors[i] = gcd_minus_one[i] * lcm_minus_one[i]

        max_minus_one = max(form_factors)
        all_together = left_gcd[-1] * left_lcm[-1]

        return max(max_minus_one, all_together)

