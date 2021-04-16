# Q22
"""
6자리의 연월일(YYMMDD)을 입력받아, 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력하시오.

ex)
input: 210316
output: 21 03 16
"""

date = input()
print(date[0:2], date[2:4], date[4:6])