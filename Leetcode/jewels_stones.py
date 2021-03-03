# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Constraints:
#   1 <= jewels.length, stones.length <= 50
#   jewels and stones consist of only English letters.
#   All the characters of jewels are unique.

# 1. Basic (32 ms)
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        answer = 0
        
        for char in stones:
            try: dict[char] += 1
            except: dict[char] = 1
        
        for char in jewels:
            if char in dict:
                answer += dict[char]
        
        return answer
"""

# 2. Using defaultdict (32 ms)
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.defaultdict(int)
        answer = 0
        
        for char in stones:
            dict[char] += 1
        
        for char in jewels:
            answer += dict[char]
        
        return answer
"""

# 3. Using Counter (32 ms)
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.Counter(stones)
        answer = 0
        
        for char in jewels:
            answer += dict[char]
        
        return answer
"""

# 4. Pythonic way (32 ms)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)