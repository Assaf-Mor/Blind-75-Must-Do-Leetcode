# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validDfs(node, leftBoundry, rightBoundry):
            if not node:
                return True
            if not (node.val > leftBoundry and node.val < rightBoundry):
                return False
            
            return validDfs(node.right, node.val, rightBoundry) and validDfs(node.left, leftBoundry, node.val)
        return validDfs(root, float("-inf"), float("inf"))
            