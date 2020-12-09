from itertools import permutations

def is_prime(x):
    if x <= 1: return False     # 0 또는 1은 소수가 될 수 없음
    else:
        i = 2
        while i * i <= x:       # x의 제곱근까지만 비교하기 위한 조건
            if x % i == 0:
                return False
            i += 1
        return True

def solution(numbers):
    new_nums = []
    answer = 0

    for i in range(1, len(numbers)+1):
        pnums = list(permutations(numbers, i))   # numbers 중 i개의 숫자의 순열
        for pnum in pnums:
            new_nums.append(int(''.join(pnum)))  # 튜플형의 자료를 문자열로 합치고, 정수형으로 리스트에 추가

    new_nums = list(set(new_nums))
    for num in new_nums:
        if is_prime(num):
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))