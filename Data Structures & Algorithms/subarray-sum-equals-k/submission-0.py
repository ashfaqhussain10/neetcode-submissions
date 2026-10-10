class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}   # empty red part, seen once
        total = 0          # bug 1: initialize, and don't shadow sum()
        res = 0            # bug 1

        for num in nums:                     # bug 2: walk nums, no n+1
            total += num                     # bug 3: whole so far
            ques = total - k                 # red = whole - k
            res += sum_map.get(ques, 0)      # bugs 4 + 5: look up red, add count
            sum_map[total] = sum_map.get(total, 0) + 1   # bug 6: record whole AFTER lookup

        return res                           # bug 7