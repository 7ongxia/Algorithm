class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        number = ""
        for i in digits:
            number += f"{i}"
        number = int(number) + 1
        number = str(number)
        for i in number:
            answer.append(int(i))
        return answer