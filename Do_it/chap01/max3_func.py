# 세 정수의 최댓값 구하기

def max3(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

print(f'max3(1, 3, 2) = {max(1, 3, 2)}')