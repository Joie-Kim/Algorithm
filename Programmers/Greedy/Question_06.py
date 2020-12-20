def solution(routes):
    check = [0] * len(routes)   # 카메라를 만났는지 확인
    answer = 0                  # 카메라 갯수

    routes.sort(reverse = True) # 진입 지점 기준 내림차순 정렬

    for i, c1 in enumerate(routes):
        if check[i] == 0:                                   # 카메라를 만난적 없는 c1
            camera = c1[0]                                  # 진입 지점에 카메라 설치
            answer += 1
        for j, c2 in enumerate(routes):
            if check[j] == 0 and c2[0] <= camera <= c2[1]:  # 카메라를 만난적 없고, 이동 경로에 카메라가 있는 c2
                check[j] = 1

    return answer

print(solution([[-20,15],[-14,-5],[-18,-13],[-5,-3]]))