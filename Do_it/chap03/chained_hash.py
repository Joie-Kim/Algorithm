# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key # 임의의 자료형
        self.value = value # 임의의 자료형
        self.next = next # 노드형

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화
        빈 해시 테이블 생성"""

        self.capacity = capacity # 해시 테이블의 크기
        self.table = [None] * self.capacity # 해시 테이블(리스트) 선언
    
    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int): # key가 int형인 경우,
            return key % self.capacity # key를 capacity로 나눔
        # 그렇지 않은 경우(문자열, 클래스, 리스트 형), hashlib 모듈에서 제공하는 방식으로 처리
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드 주목
        
        return None # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고, 값이 value인 원소 추가"""
        hash = self.hash_value(key) # 추가 하려는 키의 해시값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return False # 추가 실패
            p = p.next
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드 추가
        return True
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""

        hash = self.hash_value(key) # 삭제할 key의 해시값
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True # 삭제 성공
            pp = p
            p = p.next
        
        return False # 삭제 실패

    def dump(self) -> None:
        """해시 테이블을 덤프"""

        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()

                                                                                    