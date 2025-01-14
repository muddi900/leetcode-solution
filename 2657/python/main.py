from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        map = set()

        n = len(A)
        ans = [0] * n

        for i in range(n):
            a, b = A[i], B[i]

            if a == b:
                ans[i] += 1

            if a in map:
                ans[i] += 1

            if b in map:
                ans[i] += 1

            if i > 0:
                ans[i] += ans[i - 1]

            map.add(a)
            if a != b:
                map.add(b)

        return ans


s = Solution()

print(s.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(s.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
