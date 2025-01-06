from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)
        answer = [0] * length

        i = 0
        j = length - 1

        while i < j:
            if boxes[i] == "1":
                answer[j] += j - i

            if boxes[j] == "1":
                answer[i] += j - i

            i += 1
            j -= 1
       

        return answer
    


s = Solution()
print(s.minOperations("001011"))

# Brute Force solution(0fe98036bb0108e2c49c13fbf100ad5904d98759): Worked but the result was at the 22.84%