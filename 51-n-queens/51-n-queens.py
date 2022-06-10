class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def followsDiagonal(r1, c1, r2, c2):
            l_diagonal = r1-c1
            r_diagonal = r1+c1

            if r2-c2 == l_diagonal or r2+c2 == r_diagonal:
                return True
            else:
                return False

        def isValid(r, c):
            
            for tr, tc in visited:
                if followsDiagonal(tr, tc, r, c):
                    return False
            
            for vr, vc in visited:
                if r == vr or c == vc: return False
                
            if (r,c) in visited:
                return False
            else:
                return True

        def backtrack(r, c, queens):
            if n==1:
                grid[r][c] = "Q"
                queens-=1
                
            if queens==0:
                res.append(["".join([ "." if grid[x][y] == 0 else "Q" for y in range(n)]) for x in range(n)])
                return

            if r==n-1 and c==n-1:
                return

            for i in range(r ,n):
                c_range = list(range(c,n))+list(range(0,c))
                for j in c_range:
                    if isValid(i,j):
                        grid[i][j] = 1
                        queens-=1
                        visited.append((i, j))
                        backtrack(i+1, (j+1)%(n-1), queens)
                        visited.pop()
                        grid[i][j] = 0
                        queens+=1

        grid = [[0]*n for i in range(n)]
        visited = []
        res = []
        backtrack(0, 0, n)
        return res