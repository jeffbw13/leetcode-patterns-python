# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #traverse both trees

        def traverse(tree1, tree2):
            if (tree1 == None and tree2 == None):  # still equal
                return True;
            if (tree1 == None or tree2 == None):  # missing one
                return False

            if tree1.val == tree2.val:
                if traverse(tree1.left, tree2.left):
                    return traverse(tree1.right, tree2.right)
                else:
                    return False
            else:
                return False

        return traverse(p, q)