from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = ["()"]

        for i in range(n - 1):
            ans = self.generate(ans)

        return ans

    def generate(self, list1: List[str]):
        length = len(list1[0])
        comb = []

        for s in list1:
            for i in range(length):
                tmp = s[:i] + '()' + s[i:]
                comb.append(tmp)
        return list(set(comb))


solution = Solution()
result = solution.generateParenthesis(5)
print(result)
