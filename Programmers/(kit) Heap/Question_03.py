import heapq

def solution(operations):
    heap = []
    answer = []

    operations = list(map(lambda x: x.split(' '), operations))
    print(operations)

    for op in operations:
        print(op)
        if op[0] == 'I':                    # 삽입
            heapq.heappush(heap, int(op[1]))
            print(heap)
        else:
            print(heap)
            if len(heap) != 0:
                if op[1] == '1':                # 최댓값 삭제
                    max = heapq.nlargest(1, heap)[0]
                    print(heap)
                    heap.remove(max)
                    print(heap)
                elif op[1] == '-1':             # 최솟값 삭제
                    heapq.heappop(heap)

    if len(heap) == 0: answer = [0,0]
    else:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]

    return answer