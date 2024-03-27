# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        return self.solve(head)

    def solve(self, head):
        if head is None:
            return True

        ans = self.solve(head.next) and head.val == self.curr.val
        self.curr = self.curr.next
        return ans
