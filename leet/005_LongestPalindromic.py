class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]

        for idx, ch in enumerate(s):
            n = s.count(ch, idx + 1)
            last_idx = len(s)
            for i in range(n):
                last_idx = s.rfind(ch, idx + 1, last_idx)
                tmp = s[idx:last_idx + 1]
                if tmp == tmp[::-1]:
                    ans = ans if len(ans) > len(tmp) else tmp
                    break

        return ans

solution = Solution()
result = solution.longestPalindrome('aacabdkacaa')
print(result)