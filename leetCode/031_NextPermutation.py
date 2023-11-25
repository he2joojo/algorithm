from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 1. 뒤에서부터 <가 되는 idx 찾기
        # 2. idx = 0이면 순열의 끝이므로 reverse() 반환
        # 3. nums[idx-1]이 바뀌어야 하는 자리
        # 4. nums[idx:] 맨 뒤부터 swap < nums[i]찾아서 바꾸고
        # 5. nums[idx:]는 정렬
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
