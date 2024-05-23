# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            left_tree, right_tree = stack[-1][0], stack[-1][1]
            stack.pop()
            if not left_tree and not right_tree:
                continue
            if not left_tree and right_tree or not right_tree and left_tree or left_tree.val != right_tree.val:
                return False
            stack.append((left_tree.left, right_tree.left))
            stack.append((left_tree.right, right_tree.right))

        return True
