# [Do it! 실습 9C-1] 이진 검색 트리 클래스 BinarySearchTree 사용하기(오름차순, 내림차순으로 덤프)

from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['insert', 'remove', 'search', 'dump', 'dump_rev', 'range_key', 'exit'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()  # 이진 검색 트리를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.insert:  # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.remove:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.search:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.dump:  # 오름차순 덤프
        tree.dump()


    elif menu == Menu.dump_rev:  # 내림차순 덤프
        tree.dump(reverse = True)

    elif menu == Menu.range_key :  # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')
        
    else: # 종료
        break