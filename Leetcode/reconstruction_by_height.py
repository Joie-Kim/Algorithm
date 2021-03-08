# 406. Queue Reconstruction by Height
# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

# 92 ms
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            # 파이썬에서는 최소힙만 지원하기 때문에
            # 음수로 변환해서 최대 값이 가장 먼저 pop 되도록 한다. (FIFO)
            heapq.heappush(heap, (-person[0], person[1]))
        
        answer = []
        while heap:
            person = heapq.heappop(heap)
            # answer의 person[1] 인덱스에 값을 삽입한다.
            answer.insert(person[1], (-person[0], person[1]))
        
        return answer