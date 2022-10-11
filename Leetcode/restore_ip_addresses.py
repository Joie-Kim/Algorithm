# 93. Restore IP Addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        
        def bfs(result, rest, num):
            print(result, rest, num)
            
            if num == 3:
                if rest == str(int(rest)) and int(rest) <= 255:
                    answer.append('.'.join(result) + '.' + rest)
                return
            
            for i in range(1, len(rest)):
                n = rest[0:i]
                print('n: ', n)
                if n != str(int(n)): continue
                if int(n) > 255: return
                
                new_result = result + [n]
                bfs(new_result, rest[i:], num+1)
                    
        
        bfs([], s, 0)
        
        return answer