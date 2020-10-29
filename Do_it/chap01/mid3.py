# 세 정수의 중앙값 구하기

# 내가 짠 거
"""
def mid(a, b, c):
    if a >= b:
        if b >= c:
            middle = b
        else:
            middle = c
    else:
        if a >= c:
            middle = a
        else:
            middle = c
    
    return middle
"""

# 책에 나온 코드
def mid(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else: return c
    elif a > c:
        return a
    elif b > c:
        return c
    else: return b

print(f'mid(1, 3, 2) = {mid(1, 3, 2)}')
print(f'mid(6, 4, 3) = {mid(6, 4, 3)}')
print(f'mid(5, 8, 3) = {mid(5, 8, 3)}')