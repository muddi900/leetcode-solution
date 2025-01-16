from typing import *


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for a in nums1:
            for b in nums2:
                ans = ans ^ a ^ b

        return ans
