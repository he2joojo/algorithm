from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for i in range(len(nums)):
            tmp = nums[i]
            tmp2 = target - tmp
            if nums.count(tmp2) == 0:
                continue
            idx = nums.index(tmp2)
            if idx == i:
                continue
            answer.append(i)
            answer.append(idx)
            break
        return answer

solution = Solution()
result = solution.twoSum([2,7,11,15], 9)
print(result)
