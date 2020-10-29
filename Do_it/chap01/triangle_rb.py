# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

n = int(input('정수를 입력하세요. : '))

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()