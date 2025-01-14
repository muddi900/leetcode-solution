from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        map_a = set()
        map_b = set()

        ans = []

        for i, vals in enumerate(zip(A, B)):
            a, b = vals

            ans.append(0)

            if a == b:
                ans[i] += 1

            if a in map_b:
                ans[i] += 1

            if b in map_a:
                ans[i] += 1

            if i > 0:
                ans[i] += ans[i - 1]

            map_a.add(a)
            map_b.add(b)

        return ans


s = Solution()

print(s.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(s.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
