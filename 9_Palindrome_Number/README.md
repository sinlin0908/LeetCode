# 9. Palindrome Number

初級

## 題目

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

## 作法

轉換成 string 再用 slice 做轉換

## Code

```python
class Solution:
    def isPalindrome(self, number: int) -> bool:
        number = str(number)

        if number[::-1] != number:
            return False
        return True
```

## 效果

- Runtime: 76 ms
- Memory Usage: 13.3 MB