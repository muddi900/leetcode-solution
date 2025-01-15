class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        m = 1
        p = len(s) - 1
        start_flag = False
        for i, c in enumerate(s):
            is_number = ord("0") <= ord(c) <= ord("9")

            if not start_flag:
                if not (is_number or c in [" ", "+", "-"]):
                    break

                if c == " ":
                    continue

                if c == "-" or c == "+":
                    m = -1 if c == "-" else 1
                    start_flag = True
                    continue

                if is_number:
                    start_flag = True

            if start_flag:
                if is_number:
                    u = (ord(c) - ord("0")) * 10 ** (p - i)

                    ans += u

                if not is_number:
                    ans = ans // 10 ** (len(s) - i)
                    break

        if ans >= 2**31:
            return -(2**31) if m == -1 else 2**31 - 1
        return m * ans


s = Solution()

print(s.myAtoi(s="42"))
print(s.myAtoi(s=" -042"))
print(s.myAtoi(s="1337c0d3"))
print(s.myAtoi(s="0-1"))
print(s.myAtoi(s="+-12"))
