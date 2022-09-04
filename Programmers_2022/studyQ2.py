# link: https://school.programmers.co.kr/learn/courses/30/lessons/92335

import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

def isPrime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return False
    return True
    
def solution(n, k):
    converted_num = convert(n, k)
    converted_arr = converted_num.split('0')
    print(converted_arr)
    answer = 0
    
    for num in converted_arr:
        if num and isPrime(int(num)):
            answer += 1
    
    return answer