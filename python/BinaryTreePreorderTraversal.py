# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def __init__(self):
        self.result = []

    def __traversal(self, root):
        if root:
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.__traversal(root)
        return self.result
