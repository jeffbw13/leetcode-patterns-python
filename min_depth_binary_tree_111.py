# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
                return 0
        self.min_depth = sys.maxsize
        # every time we find a leaf, check the depth

        def traverse(node, depth):
            if node.left == None and node.right == None:  # is a leaf
                self.min_depth = min(self.min_depth, depth)
                return

            if node.left:
                traverse(node.left, depth+1)

            if node.right:
                traverse(node.right, depth+1)

        traverse(root, 1)
        return self.min_depth