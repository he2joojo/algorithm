from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dic = {nums[v]: v for v in range(len(nums))}

        if dic.get(target) is None:
            return -1

        return dic[target]

solution = Solution()
result = solution.search([4,5,6,7,0,1,2], 0)
print(result)

