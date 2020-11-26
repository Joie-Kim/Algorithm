# 고정 길이 큐 클래스(FixedQueue) 사용하기

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['enque', 'deque', 'peek', 'find', 'dump', 'exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64) # 최대 64개의 데이터를 push 할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.enque:
        x = int(input('데이터를 입력 하세요. : '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('Queue is full..')
    
    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'result : {x}')
        except FixedQueue.Empty:
            print('Queue is empty..')
    
    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f'result : {x}')
        except FixedQueue.Empty:
            print('Queue is empty..')
    
    elif menu == Menu.find:
        x = int(input('검색할 값을 입력하세요. : '))
        if x in q:
            print(f'{q.count(x)}개가 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else:
            print('검색한 값을 찾을 수 없습니다.')
    
    elif menu == Menu.dump:
        q.dump()
    
    else:
        break
