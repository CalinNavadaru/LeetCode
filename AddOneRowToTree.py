# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.inserted_left = False

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.inserted_left = False
        if depth == 1:
            new_root = TreeNode(val=val)
            new_root.left = root
            return new_root

        self.__add_one_row(root, val, depth - 1, None)
        return root

    def __add_one_row(self, node: Optional[TreeNode], val: int, depth: int, parent: Optional[TreeNode]):
        if node is None:
            return
        if depth == 1:
            if not self.inserted_left:
                new_node = TreeNode(val, node)
                parent.left = new_node
                self.inserted_left = True
                return
            elif self.inserted_left:
                new_node = TreeNode(val, right=node)
                parent.right = new_node
                return
        self.__add_one_row(node.left, val, depth - 1, node)
        self.__add_one_row(node.right, val, depth - 1, node)


a = Solution()
print(a.addOneRow(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 5, 4))
