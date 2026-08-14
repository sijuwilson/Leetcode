"""
    Level: Easy
    Problem:
    Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

    Example 1:

    Input: s = "bcbbbcba"
    Output: 4
    Explanation:
    The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

    Example 2:

    Input: s = "aaaa"
    Output: 2
    Explanation:
    The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

    Constraints:

    2 <= s.length <= 100
    s consists only of lowercase English letters.

"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        mx = 0
        left = 0
        freq = {}
        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
            if mx < right - left + 1:
                mx = right - left + 1
        return mx
