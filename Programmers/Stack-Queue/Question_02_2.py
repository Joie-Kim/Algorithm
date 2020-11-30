def solution(progresses, speeds):
    answer = []
    
    for p, s in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0] < -((p-100)//s): # // 연산: 내림 해서 몫만 구함, 음수를 내림 하면 절댓값이 +1 됨
            answer.append([-((p-100)//s), 1]) # (작업 시간, 함께 릴리즈 하는 기능 개수)를 묶어서 리스트에 저장
        else:
            answer[-1][1] += 1
    
    return [a[1] for a in answer]