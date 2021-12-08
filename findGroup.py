class Solution:
    def findGroup(self, ans, word):
        sorted_word = "".join(sorted(word))
        has_group = False
        
        if sorted_word in ans:
            ans[sorted_word].append(word)
        else:
            ans[sorted_word] = [word]
        
        return None
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            self.findGroup(ans, word)
        
        return ans.values()