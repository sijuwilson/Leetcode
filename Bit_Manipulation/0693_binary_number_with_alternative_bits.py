"""
    Level: Easy
    Problem:
    Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

    Example 1:

    Input: n = 5
    Output: true
    Explanation: The binary representation of 5 is: 101

    Example 2:

    Input: n = 7
    Output: false
    Explanation: The binary representation of 7 is: 111.

    Constraints:

    1 <= n <= 231 - 1.

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor = n ^ (n >> 1) 
        return (xor & (xor + 1)) == 0