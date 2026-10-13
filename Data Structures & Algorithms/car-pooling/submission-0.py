class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = sorted((frm, num) for num, frm, to in trips)
        drops   = sorted((to, num)  for num, frm, to in trips)
        people = 0
        i = j = 0
        while i < len(pickups):
            if pickups[i][0] < drops[j][0]:   # next event is a pickup
                people += pickups[i][1]
                i += 1
                if people>capacity:
                    return False
            else:                             # drop-off first (also on a tie)
                people -= drops[j][1]
                j += 1
        return True