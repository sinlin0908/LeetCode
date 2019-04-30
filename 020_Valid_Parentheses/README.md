# 20. Valid Parentheses

初級

## 題目

Given a string containing just the characters `'(', ')', '{', '}', '[' and ']', `determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
```
Input: "()"
Output: true
```
Example 2:
```
Input: "()[]{}"
Output: true
```
Example 3:
```
Input: "(]"
Output: false
```
Example 4:
```
Input: "([)]"
Output: false
```
Example 5:
```
Input: "{[]}"
Output: true
```

## 作法

- 後進先出 -->  Stack
- 對應的左右邊 --> hash table
- 如果符號是左邊的就放進對應的右邊到 stack
- 反之，stack Pop 出來的符號與現在的比對

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        head_list = ["(", "{", "["]
        dict_ = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for sym in s:
            if sym in head_list:
                stack.append(dict_[sym])
            else:
                if not stack:
                    return False
                correct_tail = stack.pop()
                
                if correct_tail != sym:
                    return False
        if stack:
            return False
        return True
```

## 效果

- Runtime: 36 ms, faster than 88.55% of Python3 online submissions for Valid Parentheses.
- Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.