from collections import defaultdict


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        matched = defaultdict(set)
        answer = set()

        for word in words:
            for match_word in words:

                if any(
                    [
                        match_word == word,
                        word in matched[match_word],
                        match_word in matched[word],
                    ]
                ):
                    continue

                if len(word) < len(match_word) and word in match_word:
                    answer.add(word)

                if len(match_word) < len(word) and match_word in word:
                    answer.add(match_word)

                matched[match_word].add(word)
                matched[word].add(match_word)

        return list(answer)


# HashMap based solution solves all test cases(e1cafae21233179e285135c861ffc747f3988454).


s = Solution()
print(s.stringMatching(["mass", "as", "hero", "superhero"]))
print(s.stringMatching(["leetcode", "et", "code"]))
print(s.stringMatching(["blue", "green", "bu"]))
