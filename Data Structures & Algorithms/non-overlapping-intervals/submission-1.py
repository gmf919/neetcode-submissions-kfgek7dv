class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0 
        intervals.sort()
        curr = [intervals[0]]

        for  i in range(1,len(intervals)):

            if curr[-1][1] <= intervals[i][0]:
                curr.append(intervals[i])
            else:
                res += 1
                curr[-1][1] = min(curr[-1][1], intervals[i][1])
        
        return res
            

