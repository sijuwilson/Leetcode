**Level:** Medium

**Problem:**

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

**Example 1:**

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

**Example 2:**

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

**Constraints:**

1 <= s.length <= 105, 
s consists of lowercase English letters.
1 <= k <= s.length.

**Solution: (python3)**

    class Solution:
        def maxVowels(self, s: str, k: int) -> int:
            vowels = "aeiou"
            cc = 0
            for r in range(k):
                if s[r] in vowels:
                    cc += 1
            if cc == k: return k
            mx = cc
            for r in range(k,len(s)):
                if s[r-k] in vowels: cc -= 1
                if s[r] in vowels: cc += 1
                if cc == k: return k
                mx = mx if mx > cc else cc
            return mx
