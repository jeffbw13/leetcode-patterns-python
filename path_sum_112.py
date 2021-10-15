# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # why can traverse access targetSum here??

        def traverse(node, sum):
            sum += node.val

            # is it a leaf?
            if node.left == None and node.right == None:
                if sum == targetSum:
                    return True

            if node.left and traverse(node.left, sum):
                return True
            if node.right and traverse(node.right, sum):
                return True
            return False

        if root != None:
            return traverse(root, 0)
        else:
            return False