class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        haystackLength = len(haystack)
        for i in range(haystackLength-needleLength+1):
            if haystack[i:i+needleLength] == needle:
                return i
        
        return -1