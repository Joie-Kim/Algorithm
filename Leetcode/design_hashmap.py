# 706. Design Hashmap
# Design a HashMap without using any built-in hash table libraries.
# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# 216 ms
class ListNode:
    """ 체이닝 방식을 사용하기 위해 리스트 노드 정의"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
    
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode) # 초기값이 있는 딕셔너리 사용
        

    def put(self, key: int, value: int) -> None:
        # 해쉬 함수
        index = key % self.size
        
        # 해쉬 값을 인덱스로 갖는 원소가 없을 경우 (즉, 버킷이 비었을 경우)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 원소가 있을 경우
        p = self.table[index]
        while p:
            # 이미 key 값이 존재하면 value 값을 바꾸고
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        # 일치하는 key 값이 없으면 ListNode 추가
        p.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = key % self.size
        
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        
        if self.table[index].value is None:
            return
        
        # 해당 인덱스에 있는 리스트 중 첫번째 노드에 삭제할 key 값이 있을 경우
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 첫번째를 제외한 노드에 있을 경우
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next