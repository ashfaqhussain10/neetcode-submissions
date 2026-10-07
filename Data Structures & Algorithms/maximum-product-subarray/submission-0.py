class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Maximum Product Subarray
        max_end = min_end = ans = nums[0]
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = nums[i] * min_end
            v3 = nums[i] * max_end
            max_end = max(v1, v2, v3)
            min_end = min(v1, v2, v3)
            ans = max(ans, max_end)
        return ans