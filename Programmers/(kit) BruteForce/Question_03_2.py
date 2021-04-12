# 문제에 빠진 조건 : brown은 무조건 한 줄
# 약수를 구해서 리스트로 저장하지 않고, 바로 조건문에 적음

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]