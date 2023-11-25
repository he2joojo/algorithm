from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = 0
        for i in range(len(nums) -1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx = i
                break

        if idx == 0:
            nums.reverse()
            return

        swap = nums[idx - 1]
        for i in range(len(nums)-1, idx-1, -1):
            if swap < nums[i]:
                nums[idx-1] = nums[i]
                nums[i] = swap
                break

        tmp = nums[idx:]
        tmp.sort()
        nums[idx:] = tmp

solution = Solution()
nums = [1, 3, 2]
solution.nextPermutation(nums)
print(nums)
