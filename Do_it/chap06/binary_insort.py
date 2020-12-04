# 파이썬 표준 라이브러리에서 biset 모듈의 insort() 함수로 제공되는 단순 삽입 정렬 알고리즘 사용
# 이진 삽입 정렬 구현하기

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬 (bisect.insort 사용)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)

    print('오름차순으로 정렬 완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')