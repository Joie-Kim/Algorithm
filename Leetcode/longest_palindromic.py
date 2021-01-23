# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# 244 ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롭 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)):
            # 팰린드롭의 길이가 홀수, 짝수일 경우 모두 고려
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result