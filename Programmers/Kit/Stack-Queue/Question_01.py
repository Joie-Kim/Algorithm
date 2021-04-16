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