# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = list()
        tmp = deque([root])

        while tmp:
            curr_max = float("-inf")

            for _ in range(len(tmp)):
                node = tmp.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(curr_max)
        return ans
