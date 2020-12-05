# 파이썬의 heapq 모듈은
# 힙에 원소를 추가하는 heappush() 함수와
# 힙에서 원소를 제거하는 heappop() 함수를 제공

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬(heapq.push와 heapq.pop를 사용)"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')