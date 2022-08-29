class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx,dy = [1,0,-1,0],[0,1,0,-1]
        
        def bfs(x : int, y : int):
            queue = deque([(x,y)])
            
            while queue:
                x,y = queue.popleft()
                
                for i in range(4):
                    nx,ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                        queue.append((nx,ny))
                        grid[nx][ny] = "0"
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count += 1
                    
        return count
                
                        
            