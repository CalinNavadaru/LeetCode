# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                curr.next = new_node
                list1 = list1.next
                curr = curr.next
            else:
                new_node = ListNode(list2.val)
                curr.next = new_node
                list2 = list2.next
                curr = curr.next

        curr.next = list1 or list2

        result = head.next
        del head
        return result
