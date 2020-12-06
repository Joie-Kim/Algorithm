import heapq

def solution(operations):
    heap = []
    answer = []

    operations = list(map(lambda x: x.split(' '), operations))
    print(operations)

    for op in operations:
        print(op)
        if op[0] == 'I':                    # 삽입
            heapq.heappush(heap, op[1])
            print(heap)
        else:
            print(heap)
            if len(heap) != 0:
                if op[1] == '1':                # 최댓값 삭제
                    max = heapq.nlargest(1, heap)
                    print(heap)
                    heap.remove(max)
                    print(max)
                elif op[1] == '-1':             # 최솟값 삭제
                    heapq.heappop(heap)

    if len(heap) == 0: answer = [0,0]
    else:
        answer = [heapq.nlargest(1, heap), heap[0]]

    return answer

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))