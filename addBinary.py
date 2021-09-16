class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        carry = 0
        answer = ''
        
        for i in range(maxLen-1, -1, -1):
            digit = carry
            digit += 1 if a[i] == '1' else 0
            digit += 1 if b[i] == '1' else 0
            
            answer = ('0' if (digit % 2) == 0 else '1') + answer
            carry = 1 if 1 < digit else 0

        if carry == 1:
            answer = '1' + answer
        
        return answer