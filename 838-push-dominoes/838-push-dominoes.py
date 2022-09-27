#유효한 지점들에 flg 먹이기 -> Turn 부여해서 서있는지 결정!

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left_prefix = [0] * n
        right_prefix = [0] * n
        
        for i in range(n):
            if dominoes[i] != ".":
                left_prefix[i] = 100000 if dominoes[i] == "R" else -100000
            
            else:
                left_prefix[i] = left_prefix[i-1] - 1 if (i and left_prefix[i - 1] > 0) else 0
                
            if dominoes[-i - 1] != ".":
                right_prefix[-i - 1] = 100000 if dominoes[-i-1] == "L" else -100000
            
            else:
                right_prefix[-i-1] = right_prefix[-i] - 1 if (i and right_prefix[-i] > 0) else 0
        
        print(left_prefix)
        print(right_prefix)
        return "".join(["." if left_prefix[i] == right_prefix[i] else ["L","R"][left_prefix[i] > right_prefix[i]] for i in range(n)])
            
        
        
        