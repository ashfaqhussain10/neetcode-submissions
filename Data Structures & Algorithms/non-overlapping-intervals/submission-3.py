class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        end1 = intervals[0][1]
        for start2,end2 in intervals[1:]:
            if end1 > start2 : 
                count+=1
                end1 = min(end1,end2)
            else: 
                end1 = end2
        return count
