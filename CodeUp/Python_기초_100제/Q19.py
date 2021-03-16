# Q19
"""
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력하시오.

ex)
input: 2021.03.16
output: 16-03-2021
"""

y, m, d = input().split('.')
print(d, m, y, sep='-')