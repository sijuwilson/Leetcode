"""
    Level: Hard
    Problem:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return the number of distinct solutions to the n-queens puzzle.

    Example 1:

    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

    Example 2:

    Input: n = 1
    Output: 1

    Constraints:

    1 <= n <= 9.

"""

class Solution:
    def __init__(self):
        self.cols = set()
        self.d1 = set()
        self.d2 = set()
        self.ans = 0
    def backtrack(self,row,n):
        if row == n:
            self.ans += 1
            return
        for col in range(n):
            if col in self.cols: continue
            if row - col in self.d1: continue
            if row + col in self.d2: continue

            self.cols.add(col)
            self.d1.add(row - col)
            self.d2.add(row + col)

            self.backtrack(row+1,n)

            self.cols.remove(col)
            self.d1.remove(row - col)
            self.d2.remove(row + col)

    def totalNQueens(self, n: int) -> int:
        self.backtrack(0,n)
        return self.ans