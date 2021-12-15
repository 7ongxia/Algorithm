class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda l:l[0])
        ans = []
        before = intervals[0]
        
        for interval in intervals:
            if interval[0] <= before[1] and interval[1] >= before[1]:
                if interval[1] >= before[1]:
                    before[1] = interval[1]
                if interval[0] <= before[0]:
                    before[0] = interval[0]
            elif before[0] <= interval[0] and before[1] >= interval[1]:
                continue
            else:
                ans.append(before)
                before = interval
        
        ans.append(before)
        
        return ans
