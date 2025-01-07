from collections import defaultdict


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
        answer = set()

        for i, word in enumerate(sorted_words):
            for j in range(i + 1, len(words)):
                match_word = sorted_words[j]
                if match_word in word:
                    answer.add(match_word)

        return list(answer)


s = Solution()
print(s.stringMatching(["mass", "as", "hero", "superhero"]))
print(s.stringMatching(["leetcode", "et", "code"]))
print(s.stringMatching(["blue", "green", "bu"]))
