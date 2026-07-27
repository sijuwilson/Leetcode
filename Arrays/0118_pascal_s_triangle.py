"""
    Level: Easy
    Problem:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    Example 1:

    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    Example 2:

    Input: numRows = 1
    Output: [[1]]

    Constraints:

    1 <= numRows <= 30.

"""

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        tri = [[1]]
        for i in range(1,n):
            curr = []
            prev = tri[-1]
            for j in range(i+1):
                if j == 0 :
                    curr.append(1)
                elif j == i:
                    curr.append(1)
                else:
                    ur = prev[j-1]
                    ul = prev[j]
                    curr.append(ur+ul)
            tri.append(curr)
        return tri