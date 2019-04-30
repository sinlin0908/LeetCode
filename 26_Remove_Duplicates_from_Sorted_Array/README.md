# 26. Remove Duplicates from Sorted Array

初級

## 題目

[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

## 作法

- 覆蓋 list 值就可以

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        list_len = len(nums)
        count = 0
        for i in range(list_len-1):
            if nums[i] != nums[i+1]:
                count+=1
                nums[count]=nums[i+1]
        
        return count+1
```

## 效果

- Runtime: 60 ms, faster than 80.94% of Python3 online submissions for Remove Duplicates from Sorted Array.
- Memory Usage: 14.7 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.