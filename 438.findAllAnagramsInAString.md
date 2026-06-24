**Level:** Medium
**Problem:**
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

**Example 1:**

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

**Example 2:**

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

**Constraints:**

1 <= s.length, p.length <= 3 * 104, 
s and p consist of lowercase English letters.

**Solution:(python3)**

    class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            n1 = len(p)
            n2 = len(s)
            if n1 > n2: return []
            freq1 = [0 for i in range(26)]
            freq2 = [0 for i in range(26)]
            res = []
            for i in range(n1):
                freq1[ord(p[i])-97] += 1
            for i in range(n1):
                freq2[ord(s[i])-97] += 1
            if freq1 == freq2: res.append(0)
            for i in range(n1,n2):
                freq2[ord(s[i-n1])-97] -= 1
                freq2[ord(s[i])-97] += 1
                if freq1 == freq2: res.append(i-n1+1)
            
            return res
        