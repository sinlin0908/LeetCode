# 7. Reverse Integer

初級

## 題目

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## 作法

轉換成 string 用 slice 做反轉

## Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        tmp = abs(x)
        tmp = int(str(tmp)[::-1])
        
        if tmp < -2**31 or tmp>2**31-1:
            return 0
        elif x<0:
            return tmp*-1
        else:
            return tmp
```

## 效果

- Runtime: 40 ms, faster than 99.90% of Python3 online submissions for Reverse Integer.
- Memory Usage: 13.2 MB, less than 5.71% of Python3 online submissions for Reverse Integer.