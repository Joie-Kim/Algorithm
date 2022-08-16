# 7. Reverse Integer

# (1) 정수 사용하기 (54 ms)
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        result = 0
        while x:
            result = (result * 10) + (x % 10)
            x = x // 10
        
        if -2**31 > result or 2**31 - 1 < result:
            return 0
        
        return result * sign

# (2) 문자열 사용하기 (37 ms)
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        x_string = str(x)
        result_string = x_string [::-1]
        result = int(result_string)
        
        if -2**31 > result or 2**31 - 1 < result:
            return 0
        
        return result * sign