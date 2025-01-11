from typing import *
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        c = Counter(s)

        p_count = sum([v for v in c.values() if v % 2 > 0])

        return p_count <= k


s = Solution()

print(s.canConstruct(s="annabelle", k=2))
print(s.canConstruct(s="leetcode", k=3))
print(s.canConstruct(s="true", k=4))
