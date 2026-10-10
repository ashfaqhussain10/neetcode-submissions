class NumArray:
    def __init__(self, nums: List[int]):
        # build the prefix array (length n+1, prefix[0] = 0)
        # store it on self so sumRange can use it
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(1, n+1):
            self.prefix[i] = self.prefix[i-1]+nums[i-1]
    def sumRange(self, left: int, right: int) -> int:
        # one subtraction
        return self.prefix[right+1] - self.prefix[left]