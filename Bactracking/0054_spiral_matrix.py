"""
    Level: Medium
    Problem:
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100.

"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        r, c = len(matrix), len(matrix[0])
        v = [[False]*c for _ in range(r)]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        def bt(x,y,di):
            if x < 0 or x >= r or y < 0 or y >= c or v[x][y]:
                return
            v[x][y] = True
            res.append(matrix[x][y])
            for i in range(4):
                nd = (di+i) % 4
                bt(x+dx[nd],y+dy[nd],nd)
        bt(0,0,0)
        return res