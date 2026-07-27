"""
    Level: Easy
    Problem:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]

    Example 2:

    Input: rowIndex = 0
    Output: [1]

    Constraints:

    0 <= rowIndex <= 33.

"""

class Solution:
    def getRow(self, n: int) -> List[int]:
        tri = [[1]]
        for i in range(1,n+1):
            curr = []
            prev = tri[-1]
            for j in range(i+1):
                if j == 0 or j == i:
                    curr += [1]
                else:
                    ul = prev[j-1]
                    ur = prev[j]
                    curr += [ul + ur]
            tri += [curr]
        return tri[n]