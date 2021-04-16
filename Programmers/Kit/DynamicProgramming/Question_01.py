def solution(N, number):
    if N == number: return 1                # N과 number이 같을 때, 최소값은 1
    
    nums = [set() for i in range(8)]        # N을 i번 사용해서 만들어지는 수들의 집합 리스트
                                            # (최소값이 8보다 작아야 하므로 N이 최대 8번 사용되는 경우의 수 집합)
    for i, num in enumerate(nums):
        num.add(int(str(N) * (i+1)))        # 집합에 N이 연달아 있는 경우 추가 (ex. 5, 55, 555, 5555)
    
    for i in range(1, 8):                   # N을 i번 사용했을 때
        for j in range(i):
            for n1 in nums[j]:              # N을 j번 사용한 수들과
                for n2 in nums[i-(j+1)]:    # N을 i-(j+1)번 사용한 수들의
                    nums[i].add(n1 + n2)    # 사칙 연산을
                    nums[i].add(n1 - n2)    # N을 i번 사용해서 만들어진 수를 집합에 추가 (중복 x)
                    nums[i].add(n1 * n2)
                    if n2 != 0:             # 나누는 수는 0이 되면 안 됨
                        nums[i].add(n1 // n2)
        
        if number in nums[i]:               # N을 i번 사용한 수들 중에 number가 있다면 i+1 반환
            return i+1
    
    return -1                               # N을 8번 사용한 경우에 number가 없다면 -1 반환

print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 5))