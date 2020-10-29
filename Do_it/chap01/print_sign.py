# +, - 기호 번갈아가며 출력하기

print('+, -를 번갈아 출력합니다.')
n = int(input('몇 번 출력할까요? : '))

for i in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()