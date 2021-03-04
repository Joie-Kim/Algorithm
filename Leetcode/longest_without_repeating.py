# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# 52 ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """문자열에 속한 문자를 key, 문자열에서 문자의 위치(인덱스)를 value로 갖는 해시 테이블(딕셔너리)"""
        used = {}
        max_length = start = 0
        
        for index, char in enumerate(s):
            # 슬라이싱 한 범위보다 이전에 사용된 문자일 경우, start를 이동하지 않아도 됨.
            # 따라서 start <= used[char] 조건 추가
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            
            used[char] = index
        
        return max_length