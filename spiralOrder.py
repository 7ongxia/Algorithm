class Solution:
    def getTop(self, matrix, ans):
        if matrix:
            ans += matrix.pop(0)
        return None
        
    def getRight(self, matrix, ans):
        for i in matrix:
            if i:
                ans += [i.pop()]
        return None
            
    def getBottom(self, matrix, ans):
        if matrix:
            ans += reversed(matrix.pop())
        return None
        
    def getLeft(self, matrix, ans):
        for i in reversed(matrix):
            if i:
                ans += [i.pop(0)]
        return None
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            self.getTop(matrix, ans)
            self.getRight(matrix, ans)
            self.getBottom(matrix, ans)
            self.getLeft(matrix, ans)
        return ans