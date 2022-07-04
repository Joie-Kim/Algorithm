# link: https://www.acmicpc.net/problem/6603

def combination(chosen):
    if len(chosen) == 6:
        print(*chosen)
        return
    
    start = S.index(chosen[-1]) + 1 if chosen else 0
    for i in range(start, k):
        chosen.append(S[i])
        combination(chosen)
        chosen.pop()

while True:
    input_arr = list(map(int, input().split()))
    k = input_arr[0]
    S = input_arr[1:]
    combination([])
    if k == 0:
        exit()
    print()