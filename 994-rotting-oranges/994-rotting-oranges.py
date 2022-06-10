class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        good = set()
        ans = 0
        total = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    total+=1
                    if grid[i][j] == 2:
                        q.append((i, j))
                    else:
                        good.add((i, j))
        
        if total == 0: return 0
        
        while q:
            tmp = deque()
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                for nr, nc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr += r
                    nc += c
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) in good:
                        tmp.append((nr, nc))
                        good.remove((nr, nc))
            q = tmp
            ans += 1
        return ans-1 if len(good) == 0 else -1