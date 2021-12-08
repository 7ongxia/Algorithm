class Solution:
    def dfs(self, decision_space, fixed_path, result):
        if not decision_space:
            result.append(fixed_path)
            return None
        for i in range(len(decision_space)):
            self.dfs(decision_space[:i]+decision_space[i+1:], fixed_path+[decision_space[i]], result)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result