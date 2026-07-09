"""
    Level: Medium
    Problem:
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

    Example 1:

    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Example 2:

    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

    Constraints:

    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        n1,n2 = len(s1),len(s2)
        if s1 == s2: 
            return n1
        if set(s1).isdisjoint(s2) : 
            return 0
            
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n1][n2]