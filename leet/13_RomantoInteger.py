class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(1, len(s)):
            ch1 = s[i-1]
            ch2 = s[i]
            if roman[ch1] >= roman[ch2]:
                ans += roman[ch1]
            else:
                ans -= roman[ch1]
        ans += roman[s[-1]]
        return ans

solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)