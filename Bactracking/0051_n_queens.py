"""
    Level: Hard
    Problem:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

    Example 1:

    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

    Example 2:

    Input: n = 1
    Output: [["Q"]]

    Constraints:

    1 <= n <= 9.

"""

class Solution:
    def __init__(self):
        self.cols = set()
        self.d1 = set()
        self.d2 = set()
        
    def queens(self,row,n,mat,ans):
        if row == n:
            ans.append(["".join(i) for i in mat])
            return

        for col in range(n):
            if col in self.cols:
                continue
            if row-col in self.d1: 
                continue
            if row+col in self.d2:
                continue
                    
            mat[row][col] = "Q"
            self.cols.add(col)
            self.d1.add(row - col)
            self.d2.add(row + col)
            
            self.queens(row+1,n,mat,ans)

            mat[row][col] = "."
            self.cols.remove(col)
            self.d1.remove(row - col)
            self.d2.remove(row + col)

    def solveNQueens(self, n: int) -> list[list[str]]:
        mat = [["." for i in range(n)] for _ in range(n)]
        ans = []

        self.queens(0,n,mat,ans)
        return ans
