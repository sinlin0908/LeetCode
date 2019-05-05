# 53. Maximum Subarray

初級

## 題目

[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## 想法

- continuous max : 紀錄目前連續最大
- result: 紀錄 continuous max 中最大的

- for loop 跑 list 當前 element 與 continuous max 比較

### Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = continuous_max = nums[0]
        for i in range(1,len(nums)):
            continuous_max = max(nums[i],continuous_max+nums[i])
            result = max(result,continuous_max)
        return result
```

### 效果

- O(n)
- Runtime: 72 ms, faster than 7.37% of Python3 online submissions for Maximum Subarray.
- Memory Usage: 13.8 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
