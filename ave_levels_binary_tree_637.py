# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level problem = bfs
        averages = []
        level_nodes = [root]

        while len(level_nodes):
            level_ct = len(level_nodes)
            level_tot = 0
            # process all nodes in the level
            for i in range(0, level_ct):

                node = level_nodes.pop(0)
                level_tot += node.val
                #print(level_ct, level_tot, i)
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)

            # store average for this level
            averages.append(level_tot/level_ct)

        return averages