class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = 0
        min = -10 ** 5
        sum = 0
        start = 0
        end = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if max < sum:
                max = sum
                end = i
            if sum < 0:
                start = i+1
                sum = 0
        
        if start is len(nums) and max <= 0:
            for i in nums:
                if min < i:
                    min = i
            return min
        
        return max