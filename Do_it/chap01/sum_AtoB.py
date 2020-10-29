# a부터 b까지의 정수 합 구하기

print('a부터 b까지의 정수 합을 구합니다.')
a = int(input('a의 값을 입력하세요.'))
b = int(input('b의 값을 입력하세요.'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지의 정수 합 : {sum}')