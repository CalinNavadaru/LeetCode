# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        transport = 0
        head = None
        current = None
        prev = None
        while l1 and l2:
            value = l1.val + l2.val + transport
            transport = value // 10
            value %= 10
            current = ListNode(value)
            if head is None:
                head = current
            if prev:
                prev.next = current
            prev = current
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = l1.val + transport
            transport = value // 10
            value %= 10
            current = ListNode(value)
            prev.next = current
            prev = current
            l1 = l1.next

        while l2:
            value = l2.val + transport
            transport = value // 10
            value %= 10
            current = ListNode(value)
            prev.next = current
            prev = current
            l2 = l2.next

        if transport:
            prev.next = ListNode(transport)

        return head
