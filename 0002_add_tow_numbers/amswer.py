# efinition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return []

        ans = l1.val+l2.val
        carry = 1 if ans >= 10 else 0
        head = ListNode(ans % 10)
        current = head

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

        if carry > 0:
            new_node = ListNode(carry)
            current.next = new_node

        return head
