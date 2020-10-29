# 1부터 n까지의 정수 합 구하기

print('1부터 n까지의 정수 합을 구합니다.')
n = int(input('n의 값을 입력하세요.'))

sum = 0

for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지의 정수 합 : {sum}')