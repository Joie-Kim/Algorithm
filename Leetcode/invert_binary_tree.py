# 226. Invert Binary Tree
# Invert a binary tree.

# 1. Pythonic way (32 ms)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None # 생략 가능 (파이썬은 동적 타이핑 언어이기 때문에 자동으로 None 리턴)
"""

# 2. BFS (28 ms)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root
"""

# 3. DFS (20 ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            
            if node:
                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)
        
        return root


