# 가로, 세로의 길이가 정수이고
# 넓이가 area인 직사각형에서
# 변의 길이 나열하기
# 단, 중복 허용 x (즉, 2*16과 16*2는 같은 값)

area = int(input('직사각형의 넓이를 입력하세요.'))

for i in range(1, area+1): # area번 반복
    if i * i > area: break
    if area % i: continue
    print(f'{i} * {area//i}')