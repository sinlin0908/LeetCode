# Two Sum

初級

## 題目

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

```bash
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## 作法

有查表可以考慮 hash

使用一個 hash table 來紀錄當下的 element 對照的數字 (也就是 target-num)。

當目前的 element 有在 hash keys 裡面，代表他的搭檔之前就遇到了，就可以直接return，
反之，把當前的 element 和 index 存進 hash


## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i,num in enumerate(nums):
            if num in hash_table.keys():
                return [hash_table[num],i]
            
            hash_table[target-num]=i
```

## 效率

- 整體來說是 O(n)

- Runtime: 40 ms, faster than 87.07% of Python3 online submissions for Two Sum.
- Memory Usage: 14.5 MB, less than 5.08% of Python3 online submissions for Two Sum.
