from typing import *


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:

            if word[: len(pref)] == pref:
                count += 1

        return count


s = Solution()

print(s.prefixCount(["pay", "attention", "practice", "attend"], "at"))
print(s.prefixCount(words=["leetcode", "win", "loops", "success"], pref="code"))
