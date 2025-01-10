from typing import *
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        answer = []
        counters1 = [None] * len(words1)
        counters2 = [None] * len(words2)

        for i, word in enumerate(words1):
            flag = True
            if counters1[i] is None:
                counters1[i] = Counter(word)
            for j, w in enumerate(words2):
                if counters2[j] is None:
                    counters2[j] = Counter(w)

                if not counters2[j] & counters1[i] == counters2[j]:
                    flag = False
                    break

            if flag:
                answer.append(word)

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
