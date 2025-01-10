from typing import *


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        set1 = [set(w) for w in words1]
        set2 = set("".join(words2))

        answer = []
        for i, s in enumerate(set1):
            if set2.issubset(s):
                answer.append(words1[i])

        return answer


s = Solution()

print(
    s.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["e", "o"],
    )
)
print(
    s.wordSubsets(
        words1=["amazon", "apple", "facebook", "google", "leetcode"],
        words2=["l", "e"],
    )
)
