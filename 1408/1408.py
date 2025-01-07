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


# HashMap based solution solves all test cases(e1cafae21233179e285135c861ffc747f3988454).
# Solution is fairly fast but still at 93 percentile(3d6640f93a7c515a3f4fe8bd3dccc6672ef710a4). Clearly I am being naive somewhere.
# The issue seems to be actual string matching, which is very slow.
# Sorting fixes the speed issue. The approach as not changed but sorting


s = Solution()
print(s.stringMatching(["mass", "as", "hero", "superhero"]))
print(s.stringMatching(["leetcode", "et", "code"]))
print(s.stringMatching(["blue", "green", "bu"]))
