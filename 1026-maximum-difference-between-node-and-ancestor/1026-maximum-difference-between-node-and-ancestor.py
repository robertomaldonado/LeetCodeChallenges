# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.max_ances_diff = 0

        """
        Args:
            node
            maximum value of node ancestors
            minimum value of node ancestors
        Result:
            Update the maximum difference, the current maximum value, and the current minimum value.
        """
        def recurse(node, cur_max, cur_min):
            if not node: return 
            self.max_ances_diff = max(self.max_ances_diff, abs(cur_max - node.val), abs(cur_min - node.val))
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            recurse(node.left, cur_max, cur_min)
            recurse(node.right, cur_max, cur_min)
        recurse(root, root.val, root.val)
        return self.max_ances_diff
