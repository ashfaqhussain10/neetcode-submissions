class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}   
        total = 0         
        res = 0            

        for num in nums:                     
            total += num                   
            rem = total % k               
            res += sum_map.get(rem, 0)      
            sum_map[rem] = sum_map.get(rem, 0) + 1  

        return res                        