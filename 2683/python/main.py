from typing import *


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        main = [0] * len(derived)

        main[0] = 1 if derived[-1] == 0 else 0

        return True
