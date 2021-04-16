def solution(money):
    # 첫번째 집을 터는 경우
    total = [money[0], money[0]]
    for i in range(2, len(money)-1):    # 마지막 집에 들리지 않는다.
        total.append(max(total[i-1], total[i-2] + money[i]))
    
    # 첫번째 집을 털지 않는 경우
    total2 = [0, money[1]]
    for i in range(2, len(money)):      # 마지막 집까지 탐색 한다. (방문 여부는 알 수 없다.)
        total2.append(max(total2[i-1], total2[i-2] + money[i]))
    
    return max(total[-1], total2[-1])