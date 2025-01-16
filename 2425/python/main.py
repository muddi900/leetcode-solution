from typing import *
from collections import Counter


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        x1 = x2 = 0

        n1 = len(nums1)
        n2 = len(nums2)

        if n2 % 2 > 0:
            for n in nums1:
                x1 ^= n

        if n1 % 2 > 0:
            for n in nums2:
                x2 ^= n

        return x1 ^ x2


s = Solution()

print(s.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]))
print(s.xorAllNums(nums1=[1, 2], nums2=[3, 4]))
