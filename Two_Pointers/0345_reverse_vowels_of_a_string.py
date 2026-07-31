**Level:** Easy
**Problem:**
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

**Example 1:**

Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

**Example 2:**

Input: s = "leetcode"
Output: "leotcede"

**Constraints:**

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

**Solution:(python3)**

    class Solution:
        def reverseVowels(self, s: str) -> str:
            s = list(s)
            i = 0
            j = len(s)-1
            while i < j:
                while s[i].lower() not in "aeiou" and i < j: i+=1
                while s[j].lower() not in "aeiou" and i < j: j-=1
                if  i < j:
                    c = s[i]
                    s[i] = s[j]
                    s[j] = c
                i+=1
                j-=1
            return "".join(s)