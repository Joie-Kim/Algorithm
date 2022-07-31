# link: https://www.acmicpc.net/problem/18870

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

sortedNums = sorted(list(set(nums)))
numDic = {sortedNums[i]: i for i in range(len(sortedNums))}

for num in nums:
    print(numDic[num], end=' ')