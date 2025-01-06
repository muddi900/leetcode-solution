from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)
        answer = [0] * length
        for i in range(length):
            for j in range(i+1,length):
                if boxes[j] == "1":
                    answer[i] += j - i

                if boxes[i] == "1":
                    answer[j] += j - i

        return answer
    


s = Solution()
print(s.minOperations("001011"))