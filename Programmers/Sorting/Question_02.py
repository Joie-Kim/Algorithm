# 문자열을 sorted() 하면 첫 글자를 기준으로 사전순(유니코드)으로 정렬함
# 만약 첫 글자가 같을 경우 두 번째 글자를 비교 (이후 반복)

def solution(numbers):
    answer = ''

    nums = list(sorted(map(str, numbers), key = lambda x: x*3, reverse = True))
    answer = str(int(''.join(nums)))

    return answer