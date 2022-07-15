class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        dx,dy = [1,0,-1,0],[0,1,0,-1]
        
        def bfs(sx : int, sy : int) -> int:
            queue = deque([(sx,sy)])
            visit[sx][sy] = True
            
            area = 1
            while queue:
                x,y = queue.popleft()
                
                for i in range(4):
                    nx,ny=  x + dx[i],y + dy[i]
                    
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visit[nx][ny] and grid[nx][ny]:
                        queue.append((nx,ny))
                        visit[nx][ny] = True
                        area += 1
            return area
        
        visit = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j]:
                    ans = max(ans, bfs(i,j))
        
        return ans
        
        
        
        
        
        