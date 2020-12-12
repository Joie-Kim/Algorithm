# 다른 사람의 코드에서 배울 점
# (1) 예외 사항 고려
# (2) solution 함수를 재귀로 활용

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])