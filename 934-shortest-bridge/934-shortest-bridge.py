from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        dp = [[float("inf")] * len(grid) for _ in range(len(grid))]
        visit = [[False] * len(grid) for _ in range(len(grid))]
        

        minCost = float("inf")
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:  x,y = i,j
                
        dp[x][y] = 0
        queue = deque([(x,y)])
        
        while queue:
            x,y = queue.popleft()
            if visit[x][y]: continue
                
            visit[x][y] = True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not(0 <= nx < len(grid) and 0 <= ny < len(grid) and dp[nx][ny] > dp[x][y]):  continue

                dp[nx][ny] = dp[x][y] + 1 - grid[nx][ny]
                
                if grid[nx][ny]:
                    queue.appendleft((nx, ny))
                    if dp[nx][ny]:  minCost = min(minCost,dp[nx][ny])   #바다건너 섬이면 코스트가 존재함
                else:
                    queue.append((nx,ny))
        return minCost
                



