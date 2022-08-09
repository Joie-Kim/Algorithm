# link: https://www.acmicpc.net/problem/9084

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    result = [0 for _ in range(M+1)]    # 인덱스가 특정 금액이고, 값이 경우의 수인 배열 (즉, 특정 금액을 만드는 경우의 수)
    result[0] = 1
    for coin in coins:
        for price in range(1, M+1):
            if price - coin >= 0:       # 특정 금액을 coin을 사용해 만들 수 있는 경우 (coin에 어떤 값을 더해서 만들 수 있는 경우)
                result[price] += result[price - coin]   # coin을 더해서 만들 수 있는 경우의 수를 더함
    print(result[M])