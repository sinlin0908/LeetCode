# 58. Length of Last Word

初級

## 題目

[58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

## 想法

- 先去除字串前後的空格
- 在以空格做切割，在計算最後一個 element 的長度

### Code

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return 0

        s = s.strip(' ')
        s = s.split(' ')
        return len(s[-1])
```

### 效果

- Runtime: 36 ms, faster than 82.56% of Python3 online submissions for Length of Last Word.
- Memory Usage: 13.2 MB, less than 6.04% of Python3 online submissions for Length of Last Word.