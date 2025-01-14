from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)
        map = [0] * (n + 1)
        ans = []
        count = 0

        for i in range(n):
            a, b = A[i], B[i]

            map[a] += 1
            if map[a] == 2:
                count += 1

            map[b] += 1
            if map[b] == 2:
                count += 1

            ans.append(count)

        return ans


s = Solution()

print(s.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(s.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
