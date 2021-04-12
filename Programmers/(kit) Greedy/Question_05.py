def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])    # 비용(가중치)을 기준으로 오름차순
    routes = set([costs[0][0]])         # 연결된 섬의 집합 (최소 비용을 가진 섬을 가장 먼저 들리기 때문에 해당 섬으로 초기화)

    while len(routes) != n:
        for c in costs:
            if c[0] in routes and c[1] in routes:    # 사이클(순환)을 막기 위해서
                continue
            if c[0] in routes or c[1] in routes:    # routes에 있는 섬과 연결된 섬을 찾음
                routes.update([c[0], c[1]])         # 집합은 중복 없이 추가 됨
                answer += c[2]
                c = [-1, -1, -1]
                break                               # 최소 비용을 가진 섬을 찾기 위해 처음부터 다시 반복
            

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))                           # 4
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))                   # 7
print(solution(6, [[0,1,5],[0,3,2],[0,4,3],[1,4,1],[3,4,10],[1,2,2],[2,5,3],[4,5,4]]))  # 11