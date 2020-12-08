# for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    for i in range(len(a)):
        if a[i] == key:         # 종료 조건 2: 검색 성공
            return i
    
    return -1                   # 종료 조건 1: 검색 실패


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