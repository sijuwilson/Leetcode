**Level:** Easy
**Problem:**
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

**Example 1:**

Input: s = "anagram", t = "nagaram"
Output: true

**Example 2:**

Input: s = "rat", t = "car"
Output: false

**Constraints:**

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

**Solution:(python3)**

    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s)!=len(t):
                return False
            st=set(s)
            for i in st:
                if s.count(i)!=t.count(i):
                    return False
            return True