# 오픈 주소법을 구현하는 해시 클래스 OpenHash 사용

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['add', 'delt', 'search', 'dump', 'exit']) # 메뉴 선언

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash1(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('추가할 키를 입력하세요. : '))
        val = input('추가할 값을 입력하세요. : ')
        if not hash.add(key, val):
            print('추가 실패')
    
    elif menu == Menu.delt:
        key = int(input('삭제할 키를 입력하세요. : '))
        if not hash.remove(key):
            print('삭제 실패')
    
    elif menu == Menu.search:
        key = int(input('검색할 키를 입력하세요. : '))
        tmp = hash.search(key)
        if tmp is not None:
            print(f'검색한 키를 갖는 값은 {tmp} 입니다.')
        else:
            print('검색한 데이터가 없습니다.')
    
    elif menu == Menu.dump:
        hash.dump()
    
    else:
        break