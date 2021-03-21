"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

# 44%
# Timeout Error
# Performance tests 0개 통과
"""
def solution(N, A):
    counter = [0] * N

    for a in A:
        if a == N + 1:
            counter = list(map(lambda c: max(counter), counter))
        else:
            counter[a-1] += 1
    
    return counter
"""

# 66%
# Timeout Error (time: O(N + M))
# Performance tests 0개 통과
"""
def solution(N, A):
    counter = [0] * N

    for a in A:
        if a == N + 1:
            cmax = max(counter)
            counter = [cmax] * N
        else:
            counter[a-1] += 1
    
    return counter
"""

# 100%
# 매번 counter 리스트를 업데이트 하는 게 아니라
# N+1일 때(max counter일 때), max 값을 저장하고 있다가
# 마지막에 counter 리스트에서 max 값 보다 작은 원소들만 업데이트
def solution(N, A):
    counter = [0] * N
    max_num = max_counter = 0

    for a in A:
        if a == N + 1:
            max_counter = max_num
        else:
            if (max_counter >= counter[a-1]):
                counter[a-1] = max_counter + 1
            else:
                counter[a-1] += 1
            
            max_num = max(max_num, counter[a-1])
    
    for i in range(N):
        if max_counter != 0 and max_counter > counter[i]:
            counter[i] = max_counter

    
    return counter

