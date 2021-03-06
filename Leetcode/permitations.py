# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# 40 ms
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        prev_elements=[]
        
        def dfs(elements):
            if len(elements) == 0:
                answer.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                
                dfs(next_elements)
                
                prev_elements.pop()
            
        
        dfs(nums)
        return answer

# 36 ms
# Using itertools Module
# 온라인 테스트 시에 별도의 제약 사항이 없다면 itertools 모듈을 사용해보는 것도 좋다. (물론 직접 구현하는 방법도 알고 있어야 함)
# itertools 모듈은 반복자 생성에 최적화된 효율적인 기능들을 제공하므로, 실무에서는 알고리즘으로 직접 구현하기보다는 가능하면 itertools 모듈을 사용하는 편이 낫다.
# 잘 구현된 라이브러리라 직접 구현함에 따른 버그 발생 가능성이 낮고, 효율적으로 설계된 C 라이브러리라 속도에도 이점이 있다.
# 구현의 효율성과 성능을 위해 사용한다면 최고!
# 다만, permitations() 함수가 튜플 모음을 반환하기 때문에 주의 해야 한다. (문제에서 리스트 형식을 답으로 원한다면 변환 해줘야 함)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
"""