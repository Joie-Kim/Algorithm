def solution(m, n, puddles):
    map = [[0] * (m+1) for _ in range(n+1)]             # 배열 만들고 0으로 초기화
    map[1][1] = 1                                       # 집

    for i in range(1, n+1):                             # 행 탐색
        for j in range(1, m+1):                         # 열 탐색
            if i == 1 and j == 1: continue              # 집 만나면 넘어감
            elif [j, i] not in puddles:                 # puddles에는 [m, n]으로 들어가 있으므로 [j, i]로 비교
                map[i][j] = map[i-1][j] + map[i][j-1]   # 왼쪽, 위쪽 경우의 수를 더함 (오른쪽, 아래쪽으로만 이동 가능하기 때문)

    return map[-1][-1] % 1000000007

print(solution(4, 3, [[2, 2]]))