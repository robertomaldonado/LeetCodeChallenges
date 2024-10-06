# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
Implement a recursive function longestPath which takes a TreeNode as input. It should recursively explore the entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left and right branches:
if node is None, we have reached the end of the tree, hence we should return 0;
we want to recursively explore node's children, so we call longestPath again with node's left and right children. In return, we get the longest path of its left and right children leftPath and rightPath;
if leftPath plus rightPath is longer than the current longest diameter found, then we need to update diameter;
finally, we return the longer one of leftPath and rightPath. Remember to add 1 as the edge connecting it with its parent.
Call longestPath with root.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node: return 0
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path)+1

        longest_path(root)
        return diameter