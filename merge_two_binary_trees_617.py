# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # let's try creating a new tree
        # tree = null
        def curse(root1, root2):
            if root1 == None and root2 == None:
                return None
            node = TreeNode()
            if root1:
                node.val += root1.val
            if root2:
                node.val += root2.val


            # fill out left side
            # what if one of the following is None?
            # you can eliminate this cray by doing this at start of function:
            # if root1 == None:
            #    return root2     and same for root2
            if root1:
                if root2:
                    node.left = curse(root1.left, root2.left)
                    node.right = curse(root1.right, root2.right)
                else:
                    node.left = curse(root1.left, None)
                    node.right = curse(root1.right, None)
            else:
                node.left = curse(None, root2.left)
                node.right = curse(None, root2.right)

            return node
        return curse(root1, root2)
