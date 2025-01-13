from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        c = Counter(s)

        min_size = len(s)

        for _, freq in c.items():
            if freq <= 2:
                continue

            # f - x = 2; f-2 = x

            if freq % 2 == 0:
                min_size -= freq - 2
                continue

            min_size -= freq - 1

        return min_size


s = Solution()

print(s.minimumLength("abaacbcbb"))
print(s.minimumLength("aa"))
