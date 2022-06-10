class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        
        def DFS(r, c, d):
            if grid[r][c] == 0:
                return d
            
            d+=1
            grid[r][c] = 0
            
            for nr, nc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr += r
                nc += c
                if 0 <= nr < R and 0 <= nc < C:
                    d = (DFS(nr, nc, d))
            
            return d
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, DFS(i, j, 0))
        
        return ans