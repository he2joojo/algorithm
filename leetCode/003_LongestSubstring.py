class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        word = ""

        for ch in s:
            if ch not in word:
                word += ch
            else:
                idx = word.find(ch)
                word = word[idx + 1:]
                word += ch

            max_len = max(max_len, len(word))

        return max_len

solution = Solution()
result = solution.lengthOfLongestSubstring('pwwkew')
print(result)
