"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# 88%
# time : O(N) or O(N * log(N))
# Performance test 4개 중 3개 통과
# 통과 못 한 케이스 : chaotic + many -1, 1, 2, 3 (with minus) / wrong answer
"""
def solution(A):
    A = set(A)
    missing_num = 1

    for a in A:
        if a == missing_num:
            missing_num += 1
    
    return missing_num
"""

# 100%
# 집합을 사용하지 않고, 정렬을 했음
def solution(A):
    A.sort()
    missing_num = 1

    for a in A:
        if a == missing_num:
            missing_num += 1
    
    return missing_num