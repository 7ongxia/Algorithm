class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        prev = 101
        ans = 0
        for i in range(length-1, -1, -1):
            if nums[i] >= prev:
                prev = nums[i]
                nums.pop(i)
            else:
                prev = nums[i]
                ans += 1
        
        return ans
    
            