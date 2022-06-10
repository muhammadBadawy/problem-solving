class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        def DFS(r, c):
            
            if image[r][c] == newColor:
                return
            
            if image[r][c] == oldColor:
                image[r][c] = newColor
                
                for nr, nc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr+=r
                    nc+=c
                    if 0 <= nr < R and 0 <= nc < C:
                        DFS(nr, nc)
        DFS(sr, sc)
        
        return image