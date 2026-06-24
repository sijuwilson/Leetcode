**Level:** Medium
**Problem:**
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

**Example 1:**

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

**Example 2:**

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

**Constraints:**

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

**Solution:(python3)**

    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            
            n1 = len(s1)
            n2 = len(s2)
            if n2 < n1: return False
            k = n1
            li1 = [0 for i in range(26)]
            li2 = [0 for i in range(26)]
            for i in range(n1):
                li1[ord(s1[i])-97] += 1
            for i in range(n1):
                li2[ord(s2[i])-97] += 1
            if li1 == li2: return True
            for i in range(n1,n2):
                li2[ord(s2[i-k])-97] -= 1
                li2[ord(s2[i])-97] += 1
                if li1 == li2: return True
            return False