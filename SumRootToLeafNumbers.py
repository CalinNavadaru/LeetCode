# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    stack = []

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.__sum(root)

    def __sum(self, root):
        self.stack.append(root)
        a, b, s = 0, 0, 0
        if not root.left and not root.right:
            s = int("".join([str(i.val) for i in self.stack]))
        else:
            if root.left:
                a = self.__sum(root.left)
            if root.right:
                b = self.__sum(root.right)
            s = a + b
        self.stack.pop()
        return s
