# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    ** Sol **
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        ans = list()
        # Use a queue to perform a level-order traversal of the tree. 
        # This allows us to process all nodes at the current depth before moving to the next depth.
        tmp = deque([root])

        # For each level, record the number of nodes (l) currently in the queue.
        # Initialize a variable val to hold the last node's value of the current level.
        # Dequeue each node in the current level, update val with the node's value, and enqueue the left and right children (if they exist).
        while tmp:
            tmp_len  = len(tmp)
            ans.append(tmp[-1].val)

            for _ in range(tmp_len):
                node = tmp.popleft()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return ans
        