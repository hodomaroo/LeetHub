from collections import deque

# BFS -> X번 움직여서 해당 위치로 가는 경우의 수
MOD = 10 ** 9 + 7


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0 for _ in range(maxMove)] for _ in range(n)] for _ in range(m)]
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        
        if not maxMove:
            return 0
        
        dp[startRow][startColumn][0] = 1  # -> 초기 위치
        
        totalOut = 0

        queue = deque([(startRow, startColumn, 0)])

        while queue:
            x, y, c = queue.popleft()
            if c == maxMove:
                break
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n:
                    if c + 1 < maxMove:
                        if not dp[nx][ny][c + 1]:
                            queue.append((nx, ny, c + 1))


                        dp[nx][ny][c + 1] = (dp[nx][ny][c + 1] + dp[x][y][c]) % MOD
                    
            
                else:
                    totalOut = (totalOut + dp[x][y][c]) % MOD

        print(*dp, sep="\n\n")
        return totalOut





