class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        board[1::2] = [v[::-1] for v in board[1::2]]
        
        
        
        print(*board, sep = "\n")        
        
        dp = [999] * len(board) * len(board[0])
        q = deque([0])
        dp[0] = 0
        
        while q:
            pos = q.popleft()
                
            for i in range(1,7):    
                target = pos + i
                if target >= len(board) * len(board[0]): continue
                nx,ny = target // len(board[0]), target % len(board[0])
                target = target if board[nx][ny] - 1 < 0 else board[nx][ny] - 1
                
                if dp[target] <= dp[pos] + 1: continue
                
                dp[target] = dp[pos] + 1
                q.append(target)
        #print(dp)
        return dp[-1] if dp[-1] != 999 else -1
                        
         