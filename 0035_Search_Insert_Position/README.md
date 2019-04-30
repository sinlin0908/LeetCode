# 35. Search Insert Position

## 題目

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

## 作法

- Binary Search

## Code

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return 0

        left,right = 0,len(nums)-1
        
        
        while left<=right:
            
            middle = (right+left)//2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle]>target:
                right = middle-1
            
            else:
                left = middle+1
            
        
        return middle if nums[middle] > target else middle+1
```

## 效果

Binary Search 是 O(log n)

- Runtime: 36 ms, faster than 93.72% of Python3 online submissions for Search Insert Position.
- Memory Usage: 13.6 MB, less than 5.11% of Python3 online submissions for Search Insert Position.