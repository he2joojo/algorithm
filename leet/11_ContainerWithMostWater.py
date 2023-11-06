from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_cursor = 0
        r_cursor = len(height) - 1
        max_amount = 0

        while l_cursor < r_cursor:
            left = height[l_cursor]
            right = height[r_cursor]
            water = min(left, right) * (r_cursor - l_cursor)
            max_amount = max(max_amount, water)

            if left > right:
                r_cursor += -1
            else:
                l_cursor += 1

        return max_amount

solution = Solution()
result = solution.maxArea([1,8,6,2,5,4,8,25,7])
print(result)