# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# 64 ms
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 탐색을 위한 중첩 함수 """
        def dfs(index, path):
            # 문자열이 다 만들어졌으면 result에 추가하고 종료
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                # 입력 숫자마다 반복
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        # 에외 처리
        if not digits:
            return []
        
        # 전화기에 표시된 숫자와 무자열
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
              "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        
        return result