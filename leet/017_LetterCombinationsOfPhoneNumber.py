from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_numbers = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i',], '5':['j','k','l'],
               '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

        if len(digits) == 0:
            return []

        ans = phone_numbers[digits[0]]
        if len(digits) == 1:
            return ans

        for num in digits[1:]:
            alp = phone_numbers[num] # [d,e,f]
            tmp = ans               # [a,b,c]
            ans = []
            for ch in alp:
                ans += [tmp[i] + ch for i in range(len(tmp))]

        return ans

solution = Solution()
result = solution.letterCombinations("2")
print(result)
