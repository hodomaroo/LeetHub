class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        #Get start point of one land by loop
        startX,startY = 0,0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:  startX,startY = i,j
            
        #Define dp table that dp[x][y] means the nearest distance from start point to node (x,y)
        distance = [[0] * len(grid[0]) for _ in range(len(grid))]
        q = deque([(startX,startY)])
        distance[startX][startY] = 1
        dx,dy = [0,0,1,-1],[1,-1,0,0]
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]                
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not distance[nx][ny]:
                    #if current node is water, and the next node is land, it'll be the nearest point of another land.
                    if grid[nx][ny] and not grid[x][y]:
                        return distance[x][y] - 1
                    
                    if not grid[nx][ny]:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx,ny))
                    
                    else:
                        distance[nx][ny] = distance[x][y]
                        q.appendleft((nx,ny))
            
            
        
        