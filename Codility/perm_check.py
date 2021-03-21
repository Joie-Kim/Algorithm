"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

# 75%
# 배열의 전체 합을 이용해서 풀었음
# 예외 상황 : A = [1, 4, 1]
# 전체 합이 같지만, 순열이 아닌 경우가 있음
"""
def solution(A):
    N = len(A)
    if N == 1:
        if A[0] == 1: return 1
        else: return 0
    
    answer = N * (N+1) / 2
    result = sum(A)

    if answer != result:
        return 0
    
    return 1
"""

# 100%
# 중복 값을 제외하고, 합을 비교 했음

def solution(A):
    N = len(A)
    if N == 1:
        if A[0] == 1: return 1
        else: return 0
    
    answer = N * (N+1) / 2
    result = sum(set(A))

    if answer != result:
        return 0
    
    return 1