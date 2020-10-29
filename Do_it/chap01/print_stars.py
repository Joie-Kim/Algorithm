# *을 n개 출력하되, w개마다 줄바꿈하기

print('*을 출력합니다.')
n = int(input('몇 개 출력할까요? : '))
w = int(input('몇 개마다 줄 바꿈 할까요? : '))

# 내가 짠 거
"""
for i in range(1, n+1): # n번 반복
    print('*', end='')
    if i % w == 0: # n번 판단
        print()
"""

# 개선
for _ in range(n//w): # (n/w)번 반복 -> //는 몫을 구하는 연산 기호
    print('*' * w)

rest = n % w
if rest: # 1번 판단
    print('*' * rest)