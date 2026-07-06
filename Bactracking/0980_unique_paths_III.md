**Level:** Hard

**Problem:**

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

**Example 1:**

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

Output: 2

Explanation: We have the following two paths: 

1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

**Example 2:**


Input: grid = [[0,1],[2,0]]

Output: 0

Explanation: There is no path that walks over every empty square exactly once.

Note that the starting and ending square can be anywhere in the grid.

**Constraints:**

m == grid.length

n == grid[i].length

1 <= m, n <= 20

1 <= m * n <= 20

-1 <= grid[i][j] <= 2

There is exactly one starting cell and one ending cell.

**Solution: (python3)**

    class Solution:
        def uniquePathsIII(self, grid: List[List[int]]) -> int:
            r,c = len(grid),len(grid[0])
            s = [[0]*c for _ in range(r)]
            self.count = 0
            moves = [(1,0),(0,1),(-1,0),(0,-1)]
            totcells = 0

            def bt(x,y,ccells):
                if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] == -1 or s[x][y] == 1:
                    return 
                if grid[x][y] == 2:
                    if totcells == ccells:self.count+=1
                    return
                s[x][y] = 1

                for nx,ny in moves:
                    bt(x+nx,y+ny,ccells+1)
                
                s[x][y] = 0

            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1:
                        sx,sy = i,j
                    if grid[i][j] >= 0 :
                        totcells += 1

            bt(sx,sy,1)
            return self.count