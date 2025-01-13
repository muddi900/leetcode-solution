from collections import deque


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if s[0] == ")" and locked[0] == 1:
            return False

        is_open = False

        for p, l in zip(s, locked):
            if not is_open:
                if p == ")":
                    if l == "1":
                        return False
                    is_open = True
                    continue

                if p == "(":
                    is_open = True
                    continue

            if is_open:
                if p == ")":
                    is_open = False
                    continue

                if p == "(":
                    if l == "1":
                        return False

                    is_open = False

        return not is_open


s = Solution()
print(s.canBeValid(s="))()))", locked="010100"))
print(s.canBeValid(s="()()", locked="0000"))
print(s.canBeValid(s=")", locked="0"))
