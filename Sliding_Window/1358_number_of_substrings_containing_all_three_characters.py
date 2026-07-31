**Level:** Medium

**Problem:**

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

**Example 1:**

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

**Example 2:**

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

**Constraints:**

3 <= s.length <= 5 x 10^4, 

s only consists of a, b or c characters.

**Solution: (python3)**

    class Solution:
        def numberOfSubstrings(self, s: str) -> int:
            #s1 = {'a','b','c'}
            n = len(s)
            d = {'a':0,'b':0,'c':0}
            count = 0
            l = 0
            for r in range(n):
                d[s[r]] += 1

                while  d['a'] > 0 and d['b'] > 0 and d['c'] > 0:
                    count += n - r
                    d[s[l]] -= 1
                    l += 1
            return count