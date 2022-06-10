class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        visited = set()
        q = deque()
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            r, c = q.popleft()
            for nr, nc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr += r
                nc += c
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1
                    visited.add((nr, nc))
                    q.append((nr, nc))
        
        return mat