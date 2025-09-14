from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            queue = deque()
            visit.add((r,c))
            queue.append((r,c))

            while queue:
                row,col=queue.popleft()
                directions=[[0,1],[1,0],[-1,0],[0,-1]] #limn,lta7t,lfu9,lisr
                
                for dr,dc in directions:
                    r,c=dr+row, dc+col
                    if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visit):
                        queue.append((r,c))
                        visit.add((r,c)) 
                    

        count =0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    count+=1
        return count
