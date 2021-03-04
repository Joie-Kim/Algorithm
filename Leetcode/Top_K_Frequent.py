# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.

# 1. Using Counter (104 ms)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        answer = list()
        for _ in range(k):
            answer.append(heapq.heappop(freqs_heap)[1])
        
        return answer

# 2. Pythonic way (96 ms)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
"""