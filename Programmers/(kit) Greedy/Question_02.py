# ord() : 특정한 문자를 아스키 코드 값으로 변환해주는 함수
# chr() : 아스키 코드 값을 문자로 변환해주는 함수 (10, 16진수 사용 가능)

def solution(name):
    change = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]  # 특정 문자로 바꾸는 횟수 중 최소값 (up, down)
    idx = 0                                                                 # change 리스트의 인덱스
    answer = 0                                                              # 조이스틱 조작 횟수

    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0: return answer           # name으로 변환 완료

        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        answer += left if left < right else right   # 최소 이동 횟수를 answer에 더함
        idx += (-left) if left < right else right   # 다음에 비교할 change 원소가 있는 곳으로 인덱스 이동