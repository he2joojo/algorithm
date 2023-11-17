class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(':')', '{':'}', '[':']', ')':False, '}':False, ']':False}
        que = ''
        for ch in s:
            if parentheses[ch]:
                que += parentheses[ch]
                continue
            if len(que) == 0:
                return False
            if que[-1] != ch:
                return False
            que = que[:-1]
        return len(que) == 0

solution = Solution()
result = solution.isValid("[]")
print(result)
