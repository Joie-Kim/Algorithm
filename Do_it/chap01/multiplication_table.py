# 구구단 곱셈표 출력하기

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i*j:3}', end='') # 값을 3자리로 출력
    print() # 행 바꿈
