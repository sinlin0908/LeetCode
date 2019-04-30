# 21. Merge Two Sorted Lists

初級

## 題目

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## 作法

- 用 while loop 跑 L1 L2，做比大小，把值放到新的 Linked List

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
    
        if not l2:
            return l1
        
        if not l1 and not l2:
            return None
        
        head = current = ListNode(0)
        while l1 and l2:
            
            if l1.val < l2.val:
                current.next =l1
                l1 = l1.next
                
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
            

        current.next = l1 if l1 else l2
            

        return head.next
```

## 效果

- Runtime: 44 ms, faster than 89.05% of Python3 online submissions for Merge Two Sorted Lists.
- Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.