# 정렬 순서를 오름차순으로 하면 아래 풀이처럼 할 수 있음

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

c1 = [3, 0, 6, 1, 5]
c2 = [1, 12, 11, 9, 10, 8]
c3 = [1, 6, 6, 6, 6, 6]
c4 = [21, 20, 23, 22]
c5 = [4, 4, 4]

print(solution(c1))
print(solution(c2))
print(solution(c3))
print(solution(c4))
print(solution(c5))