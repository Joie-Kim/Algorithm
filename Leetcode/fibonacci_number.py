# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

# 1. Using brute force (796 ms / 14.3 MB)
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
"""

# 2. Using Memoization (32 ms / 14.2 MB)
# 하향식(Top-Down) 풀이 (재귀 구조)
"""
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # 저장된 값이 있으면 계산하지 않고, 그 값을 사용한다.
        if self.dp[n]:
            return self.dp[n]
        
        # 저장된 값이 없으면 계산하고, 저장한다.
        self.dp[n] = self.fib(n - 1) + self.fib(n -2)

        return self.dp[n]
"""

# 3. Using Tabulation (28 ms / 14.1 MB)
# 상향식(Bottom-Up) 풀이 (반복 구조)
"""
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        self.dp[1] = 1
        
        for i in range(2, n+1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        
        return self.dp[n]
"""

# 4. Using just two variables (16ms / 14 MB)
# 2개의 변수만 사용하기 (반복 구조)
# 2, 3번 방법에 비해 공간 복잡도가 O(n)에서 O(1)로 줄어든다.
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        
        for _ in range(0, n):
            x, y = y, x + y
        
        return x

