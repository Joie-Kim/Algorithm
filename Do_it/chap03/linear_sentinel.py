# 선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)  # seq 복사
    a.append(key)           # 복사한 배열의 끝에 검색할 값 추가

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    X = [None] * num

    for i in range(num):
        X[i] = int(input(f'X[{i}]: '))
    
    ky = int(input('검색할 값을 입력하세요.: '))

    idx = seq_search(X, ky)

    if idx == -1:
        print('검색할 값이 없습니다.')
    else:
        print(f'검색값은 X[{idx}]에 있습니다.')