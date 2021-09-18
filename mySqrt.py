class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        mid = 0
        high = x
        answer = None
        
        while answer != mid:
            answer = mid
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid
            else:
                high = mid
        
        return answer