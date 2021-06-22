"""
Time Complexity : O(n^2).
Space Complexity : O(n^2).
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.target = None 
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.target = targetSum
        
        def helper(root, cursum, path):
            
            if not root:
                return 
            
            path.append(root.val)
            cursum += root.val
            helper(root.left, cursum, list(path))
            
            if not root.left and not root.right:
                if cursum == self.target:
                    self.result.append(path)
            helper(root.right, cursum, list(path))
        
        
        helper(root, 0, [])
        return self.result