# Add two numbers

中等

## 題目

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```code
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## 作法

1. 兩數相加大於 10 要進位
2. 先產生第一個 node，且使用 `current`來做跌代

```python
ans = l1.val+l2.val
carry = 1 if ans >= 10 else 0
head = ListNode(ans % 10)
current = head
```

3. 用 `while` loop 跑一次，如果兩個都是 `None`就跳出，這樣兩個 list 不一樣長也可以計算到

```python
l1, l2 = l1.next, l2.next

while l1 or l2:
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0

    ans = x + y + carry
    carry = 1 if ans >= 10 else 0
    new_node = ListNode(ans % 10)
    current.next = new_node
    current = current.next

    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
```

4. 最後判斷 `carry` 是否還有值 ex: 900 + 100 -> carry 要多一個 node

```python
if carry > 0:
    new_node = ListNode(carry)
    current.next = new_node
```
