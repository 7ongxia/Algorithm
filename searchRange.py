from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        if not nums:
            return answer
    
        l_i = min(bisect_left(nums, target), len(nums)-1)
        r_i = bisect_right(nums, target) - 1
        
        answer[0] = l_i if nums[l_i] == target else -1
        answer[1] = r_i if nums[r_i] == target else -1
        
        return answer