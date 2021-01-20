# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# 1. Using two pointer (200 ms)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
"""

# 2. Pythonic way (176 ms)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
"""

# 3. Pythonic way 2 (204 ms)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        # 이 문제에서 공간 제약이 O(1)이었기 때문에 s = s[::-1]을 사용하면 코드 통과가 안 된다.

