def solution(tickets):
    answer = []

    # 티켓 그래프 생성
    dic_ticket = {}
    for ticket in tickets:
        try: dic_ticket[ticket[0]].append(ticket[1])
        except: dic_ticket[ticket[0]] = [ticket[1]]
    # 도착지 정렬
    for key in dic_ticket.key():
        dic_ticket[key].sort(reverse=True)

    def dfs():
        stack = ["ICN"]
        path = []                                           # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:                               # stack이 비어있을 때까지
            top = stack[-1]
            if top not in dic_ticket or len(dic_ticket[top]) == 0:  # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
                path.append(stack.pop())
            else:
                stack.append(dic_ticket[top].pop(0))
        return path[::-1]

    answer = dfs()
    return answer