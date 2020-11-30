# 첫번째 시도
# 스택, 큐 사용 없이 생각의 흐름대로 구현
# 런타임 에러 발생
"""
def solution(prices):
    answer = []
    
    for ptr in range(len(prices)):
        time = 0
        for i in range(ptr+1, len(prices)):
            if(p[i] < p[ptr]):
                answer[ptr] = time + 1
                break
        answer[ptr] = time
    
    return answer
"""

# 두번째 시도
# 위 코드에서 ptr+1 부터 length 까지의 반복문 개선을 위해
# python의 deque 모듈을 사용해 구현
def solution(prices):
    from collections import deque

    answer = []

    deque_prices = deque(prices)

    while deque_prices:
        price = deque_prices.popleft()
        time = 0
        for next_price in deque_prices:
            time += 1
            if next_price < price: break
        answer.append(time)

    return answer