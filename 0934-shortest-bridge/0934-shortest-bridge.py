class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        _x,_y = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:  _x,_y = i,j
            
        
        q = deque([(_x,_y)])
        visit = [[0] * len(grid[0]) for _ in range(len(grid))]
        visit[_x][_y] = 1
        dx,dy = [0,0,1,-1],[1,-1,0,0]
        
        while q:
            x,y = q.popleft()
            print(x,y)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]                
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visit[nx][ny]:
                    visit[nx][ny] = True
                    
                    if not grid[nx][ny]:
                        visit[nx][ny] = visit[x][y] + 1
                        q.append((nx,ny))
                    else:
                        if not grid[x][y]:
                            return visit[x][y] - 1
                        
                        visit[nx][ny] = visit[x][y]
                        q.appendleft((nx,ny))
        
        #rint(visit)
            
            
        
        