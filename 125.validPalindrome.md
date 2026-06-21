**Level:** Easy
**Problem:**
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

**Example 1:**

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

**Constraints:**

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

**Solution:(python3)**

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            if len(s)<=1:return True
            s=s.lower()
            s1 = ""
            for i in s:
                if i.isalnum():
                    s1+=i
            return s1 == s1[::-1]