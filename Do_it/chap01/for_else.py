# else문이 뒤따르는 for문 사용
# 10 ~ 99 사이의 난수 n개 생성하기

import random

n = int(input('난수를 몇 개 생성할까요? : '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break

else: # break로 for문을 빠져나오고 나오면 무시됨.
    print('\n난수 생성을 종료합니다.')