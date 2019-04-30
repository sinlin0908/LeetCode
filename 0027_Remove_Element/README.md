# 27. Remove Element

初級

## 題目

[27. Remove Element](https://leetcode.com/problems/remove-element/)

## 作法

- 覆蓋 list element

## Code

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        
        count = 0
        
        for i in range(nums_len):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1        
            
        return count
```

## 效果

- Runtime: 36 ms, faster than 99.37% of Python3 online submissions for Remove Element.
- Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Remove Element.