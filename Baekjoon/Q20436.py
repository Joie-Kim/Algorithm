# link: https://www.acmicpc.net/problem/20436
# 다시 풀어볼 것

sl, sr = map(str, input().split())
data = input()
result = 0

# x, y 좌표 찾는 함수
def find_location(word):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]

    for i, key in enumerate(keyboard):
        if word in key:
            x = key.index(word)
            y = i
            return x, y

# 키보드 왼쪽 영역에 있는 글자
left_field = 'qwertasdfgzxcv'

# data 순회하면서 거리 찾기
for d in data:
    if sl == d or sr == d: result += 1
    else:
        slx, sly = find_location(sl)
        srx, sry = find_location(sr)
        dx, dy = find_location(d)

        if d in left_field:
            result += abs(slx-dx) + abs(sly-dy) + 1
            sl, slx, sly = d, dx, dy
        else:
            result += abs(srx-dx) + abs(sry-dy) + 1
            sr, srx, sry = d, dx, dy

print(result)