class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums[:-1]:
            return True
        
        length = len(nums)
        
        # find max index
        max_index = 0
        for i in range(length-1):
            if nums[i] == 0 and max_index <= i:
                return False
            if max_index < i + nums[i]:
                max_index = i + nums[i]
        
        return True