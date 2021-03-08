# 621. Task Scheduler
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# 1440 ms
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """ 우선순위 큐를 사용하면 원소를 하나 제거할 때마다 다시 재정렬을 해줘야 함
            Counter 모듈의 most_common()을 사용해 해결 (다만, 모듈을 많이 사용해 성능이 좋지 못 했음) """

        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            # idle 사용 횟수를 줄이기 위해 n+1
            for task in counter.most_common(n+1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 원소를 목록에서 완전히 제거하는 트릭
                counter += collections.Counter()
            
            if not counter:
                break
            
            # idle 갯수를 더해준다.
            result += n - sub_count + 1
        
        return result