def word_check(begin, words) -> bool:
    """begin과 words이 한 글자 차이인지 확인하는 함수"""
    cnt = 0
    for x, y in zip(begin, words):
        if x == y: cnt += 1
    
    if cnt != len(begin)-1: return False

    return True

def solution(begin, target, words):
    nows = [begin, ]    # 현재 비교 단어
    answer = 0

    if target in words:
        while True:
            tmps = []   # words 중 now(비교 단어)와 한 글자 차이나는 단어 리스트
            for now in nows:
                for word in words:
                    if word_check(now, word) and word != target:    # 조건 (1)
                        tmps.append(word)
                        words.remove(word)
                    elif word_check(now, word) and word == target:  # 조건 (2)
                        return answer + 1                           # 실행 완료
            
            if len(tmps) == 0: return 0                             # 조건에 맞는 단어가 words에 없을 경우 (0 반환)
            
            answer += 1
            nows = list(set(tmps[:]))
    
    else:           # target이 words 안에 없으면 변환할 수 없음 (0 반환)
        return 0

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))          # target이 words에 없는 경우 (0 반환)
print(solution("hit", "cog", ["hot", "dot", "lot", "cog"]))                 # target이 words에 있지만, target이 될 수 없는 경우 (0 반환)