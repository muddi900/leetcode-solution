from typing import *


class Solution:
    def isPrefixAndSuffix(self, substring: str, string: str) -> bool:
        sublen = len(substring)
        return string[:sublen] == substring and string[-sublen:] == substring

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(word, words[j]):
                    count += 1
        return count


s = Solution()
print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
print(s.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
print(s.countPrefixSuffixPairs(["abab", "ab"]))
