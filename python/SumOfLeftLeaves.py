# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.__sum_left_leaves(root, left=False)

    def __sum_left_leaves(self, root, left):
        if not root:
            return 0
        if left and not root.left and not root.right:
            return root.val

        return self.__sum_left_leaves(root.left, True) + self.__sum_left_leaves(root.right, False)
