**Level:** Easy

**Problem:**

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

**Example 1:**

Input: s = "Hello World"

Output: 5

Explanation: The last word is "World" with length 5.

**Example 2:**

Input: s = "   fly me   to   the moon  "

Output: 4

Explanation: The last word is "moon" with length 4.

**Constraints:**

1 <= s.length <= 104, 
s consists of only English letters and spaces ' '. 
There will be at least one word in s.

**Solution: (python)**

    class Solution:
        def lengthOfLastWord(self, s: str) -> int:
            st = s.strip()
            count = 0
            i = len(st)-1
            while i >= 0 and st[i] != " ":
                count+=1
                i-=1
            return count
