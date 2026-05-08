# Definition for a binary tree node.
from same_tree import Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(Solution):
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root == None and subRoot != None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check