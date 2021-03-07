# 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# Return true if you can finish all courses. Otherwise, return false.

# Time Limit Exceeded
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 만들기
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        def dfs(x):
            # 이미 방문한 적 있다면 (순환 체크)
            if x in traced:
                return False
            
            traced.add(x)
            
            for y in graph[x]:
                if not dfs(y):
                    return False
            
            traced.remove(x)
            return True
        
        # 출발점을 다르게 해서 순환 체크
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
"""

# Improved way (92 ms)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set() # 특정 노드에서 출발해서 방문한 곳을 저장
        visited = set() # 확인 했더니 순환이 없는 노드들을 저장
        
        def dfs(x):
            if x in traced:
                return False
            if x in visited:    # 순환 없는 노드 집합에 있다면
                return True     # 이 또한 순환이 없을 것
            
            traced.add(x)
            
            for y in graph[x]:
                if not dfs(y):
                    return False
            
            traced.remove(x)
            visited.add(x)      # True일 경우에만 집합에 저장
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True