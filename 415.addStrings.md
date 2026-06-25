**Level:** Easy
**Problem:**
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

Input: num1 = "11", num2 = "123"
Output: "134"

**Example 2:**

Input: num1 = "456", num2 = "77"
Output: "533".

**Constraints:**

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

**Solution: (python3)**

    import sys
    class Solution:
        def addStrings(self, num1: str, num2: str) -> str:
            sys.set_int_max_str_digits(10000)
            n1 = 0
            n2 = 0
            for i in num1:
                n1 = (n1*10)+(ord(i)-48)
            for i in num2:
                n2 = (n2*10)+(ord(i)-48)
            
            return f"{n1+n2}"