class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_negative = True if dividend < 0 else False
        divisor_negative = True if divisor < 0 else False
        
        dividend = abs(max(-2**31, dividend) if dividend < 0 else min(2**31 - 1, dividend))
        divisor = abs(max(-2**31, divisor) if divisor < 0 else min(2**31 - 1, divisor))
        if (dividend_negative and divisor_negative) or (not dividend_negative and not divisor_negative):
            answer = dividend // divisor
        else:
            answer = -(dividend // divisor)
        
        return max(-2**31, answer) if answer < 0 else min(2**31 - 1, answer)