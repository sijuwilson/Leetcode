**Level:** Easy
**Problem:**
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

**Example 1:**

Input: s = "ab-cd"
Output: "dc-ba"

**Example 2:**

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

**Constraints:**

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

**Solution:(python3)**

    class Solution:
        def reverseOnlyLetters(self, s: str) -> str:
            i = 0
            j = len(s)-1
            l= list(s)
            while i < j:
                if l[i].isalpha() and l[j].isalpha():
                    l[i],l[j]=l[j],l[i]
                    i+=1
                    j-=1
                elif not(l[i].isalpha())and not(l[j].isalpha()):
                    i+=1
                    j-=1
                elif not(l[i].isalpha()):
                    i+=1
                else:
                    j-=1
            return "".join(l)
        