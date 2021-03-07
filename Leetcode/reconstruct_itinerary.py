# 332. Reconstruct Itinerary
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# 80 ms
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        
        # 티켓 그래프 생성
        dict_tickets = {}
        for ticket in tickets:
            try: dict_tickets[ticket[0]].append(ticket[1])
            except: dict_tickets[ticket[0]] = [ticket[1]]
        
        # 도착지를 사전순으로 정렬
        for start in dict_tickets:
            dict_tickets[start].sort()
        
        # dfs
        def dfs():
            stack = ["JFK"]
            path = []
            
            while len(stack) > 0:
                top = stack[-1]
                # top이 출발지로 있는지, top이 출발지인 티켓을 다 소비했는지 확인
                if top not in dict_tickets or len(dict_tickets[top]) == 0:
                    path.append(stack.pop())
                else:
                    stack.append(dict_tickets[top].pop(0))    
            
            return path[::-1]
        
        answer = dfs()
        return answer
"""

# Another way 1 (80 ms)
# dfs에서 재귀 호출 사용
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 기본 값이 리스트인 딕셔너리 정의
        dict_tickets = collections.defaultdict(list)
        # tickets을 미리 정렬한 뒤에 리스트에 추가
        for f, t in sorted(tickets):
            dict_tickets[f].append(t)
        
        answer = []
        def dfs(f):
            # 티켓을 모두 소비할 때까지 반복
            while dict_tickets[f]:
                dfs(dict_tickets[f].pop(0))
            answer.append(f)
        
        dfs("JFK")
        return answer[::-1]
"""

# Another way 2 (80 ms)
# 역순으로 정렬해서 pop(0)이 아닌 pop() 사용하기
# pop(0)의 시간 복잡도는 O(n)이고, pop()은 O(1)이기 때문에
# 다만, key의 value 리스트가 크지 않아서인지 성능 개선을 확인할 수는 없었음..
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict_tickets = collections.defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            dict_tickets[f].append(t)
        
        answer = []
        def dfs(f):
            while dict_tickets[f]:
                dfs(dict_tickets[f].pop())
            answer.append(f)
        
        dfs("JFK")
        return answer[::-1]