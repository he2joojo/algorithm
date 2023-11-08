from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 가장 긴 접두사 찾기
        # 정렬 후 맨 앞, 맨 뒤 공통 접두사 찾기
        strs.sort()

        ans = ''
        tmp1 = strs[0]
        tmp2 = strs[-1]
        n = min(len(tmp1), len(tmp2))

        for i in range(n):
            if tmp1[i] == tmp2[i]:
                ans += tmp1[i]
            else:
                break

        return ans

solution = Solution()
result = solution.longestCommonPrefix(["dog","racecar","car"])
print(result)