def bf_match(txt, pat):
    pt = 0      # txt 커서
    pp = 0      # pat 커서
    cnt = 0     # 정답 개수

    while pt != len(txt):
        if pp == len(pat): pp = 0
        if txt[pt] == pat[pp]: cnt += 1
        
        pt += 1
        pp += 1
    
    return cnt

def solution(answers):
    score = [None] * 3
    answer = []

    ptn1 = [1, 2, 3, 4, 5]
    ptn2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ptn3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score[0] = bf_match(answers, ptn1)
    score[1] = bf_match(answers, ptn2)
    score[2] = bf_match(answers, ptn3)

    winner = max(score)

    for i in range(len(score)):
        if winner == score[i]:
            answer.append(i+1)
    
    return answer if len(answer)==1 else sorted(answer)

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))