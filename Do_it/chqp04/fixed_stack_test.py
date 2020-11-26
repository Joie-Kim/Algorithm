# 고정 길이 스택 클래스(FixedStack) 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'find', 'dump', 'exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64) # 최대 64개의 데이터를 push 할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        x = int(input('데이터를 입력 하세요. : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('Stack is full..')
    
    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'result : {x}')
        except FixedStack.Empty:
            print('Stack is empty..')
    
    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'result : {x}')
        except FixedStack.Empty:
            print('Stack is empty..')
    
    elif menu == Menu.find:
        x = int(input('검색할 값을 입력하세요. : '))
        if x in s:
            print(f'{s.count(x)}개가 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색한 값을 찾을 수 없습니다.')
    
    elif menu == Menu.dump:
        s.dump()
    
    else:
        break
