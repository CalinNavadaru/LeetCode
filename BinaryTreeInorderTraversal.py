from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = []

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.__inorder(root)
        return [i.val for i in self.result]

    def __inorder(self, root):
        if root:
            if root.left:
                self.__inorder(root.left)
            self.result.append(root)
            if root.right:
                self.__inorder(root.right)
            return
        return
