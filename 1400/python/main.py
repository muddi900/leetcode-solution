from typing import *
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        c = Counter(s)

        p_count = len([v for v in c.values() if v % 2 > 0])

        return p_count <= k


s = Solution()

print(s.canConstruct(s="cr", k=7))
