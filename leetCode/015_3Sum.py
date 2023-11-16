from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums 정렬
        # nums 음수, 양수로 구분
        # 0이 있을 때, 절대값이 존재하는지 확인
        # 각 리스트 돌면서 조회
        # 이중 for문으로 2개 꺼내서 합이 다른 리스트에 있는지 확인

        ans = []
        nums.sort()
        nums_dict = {k: 0 for k in nums}

        negative = [i for i in nums if i < 0]
        positive = [i for i in nums if i > 0]
        exist_zero = True if 0 in nums else False

        if nums.count(0) >= 3:
            ans.append([0, 0, 0])

        if exist_zero:
            for i in positive:
                if -i in nums_dict:
                    ans.append([-i, 0, i])

        for i in range(len(negative) - 1):
            for j in range(i + 1, len(negative)):
                num1 = negative[i]
                num2 = negative[j]
                if -(num1 + num2) in nums_dict:
                    ans.append([num1, num2, -(num1 + num2)])

        for i in range(len(positive) - 1):
            for j in range(i + 1, len(positive)):
                num1 = positive[i]
                num2 = positive[j]
                if -(num1 + num2) in nums_dict:
                    ans.append([-(num1 + num2), num1, num2])

        tmp = []
        for i in ans:
            if i not in tmp:
                tmp.append(i)
        ans = tmp

        return ans


solution = Solution()
result = solution.threeSum([-2,0,0,2,2])
print(result)
