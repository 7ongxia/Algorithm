class Solution:
    def get_factorial(self, n):
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer
    
    def climbStairs(self, n: int) -> int:
        # divide by 2, and count how many 2 steps for max
        steps = [0, 0, 0]
        steps[2] = n // 2
        steps[1] = n % 2
        
        if steps[2] == 0:
            return 1
        
        # calculate the number of cases
        while steps[2] != -1:
            steps[0] += (self.get_factorial(steps[1] + steps[2]) / (self.get_factorial(steps[1]) * self.get_factorial(steps[2])))
            steps[2] -= 1
            steps[1] += 2
        
        return int(steps[0])
        