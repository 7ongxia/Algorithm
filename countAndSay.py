import itertools as it

class Solution:
    def countAndSay(self, n: int) -> str:
        def say(n):
            sentence = ""
            for k, g in it.groupby(n):
                sentence += str(len(list(g))) + k
            return sentence
        
        ans = '1'
        
        if n == 1:
            return ans
        
        for i in range(2, n+1):
            ans = say(ans)
            
        return ans