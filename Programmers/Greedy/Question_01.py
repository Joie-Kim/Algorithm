def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = 0

    for spare in new_reserve:
        if spare-1 in new_lost:
            new_lost.remove(spare-1)
        elif spare+1 in new_lost:
            new_lost.remove(spare+1)

    answer = n - len(new_lost)

    return answer

print(solution(5, [2,4,3], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))