**Level:** Easy
**Problem:**
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

**Example 1:**

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

**Example 2:**

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

**Constraints:**

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

**Solution:(python3)**

    class Solution:
        def mergeAlternately(self, word1: str, word2: str) -> str:
            i = j = 0
            res = ""
            s1,s2 = len(word1),len(word2)
            while i < s1 and j < s2:
                res+=word1[i]+word2[j]
                i+=1
                j+=1
            if i < s1:res+=word1[i:]
            if j < s2:res+=word2[j:]
            return res
