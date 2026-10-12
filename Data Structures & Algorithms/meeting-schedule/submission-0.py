class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Handle empty lists gracefully
        if not intervals:
            return True
            
        # 1. Sort by the 'start' attribute of the Interval objects
        intervals.sort(key=lambda x: x.start)
        
        # 2. Initialize our tracking using the first interval object's attributes
        end1 = intervals[0].end

        # 3. Iterate through the remaining intervals
        for item in intervals[1:]:
            # If the next meeting starts before the current one ends, there is a conflict
            if item.start < end1:
                return False
            # Update the end time to the current meeting's end
            end1 = item.end

        # If no overlaps are found, they can attend all meetings
        return True
