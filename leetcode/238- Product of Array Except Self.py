class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left_product = []
        cumul = 1
        for num in nums:
            cumul *= num
            left_product.append(cumul)

        right_product = [0] * len(nums)
        cumul = 1
        for i in range(len(nums)-1, -1, -1):
            cumul *= nums[i]
            right_product[i] = cumul

        ans = []
        for i in range(len(nums)):
            val = 1
            if i > 0:
                val *= left_product[i-1]
            if i < len(nums) - 1:
                val *= right_product[i+1]

            ans.append(val)
        
        return ans