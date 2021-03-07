# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# 48 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """ 리프 노드에서 루트 노드까지 올라오면서 거리를 계산한다.
            루트 노드까지 올라왔을 때, 왼쪽 서브 트리의 깊이와 오른쪽 서브 트리의 깊이를 더한 값이 longest가 됨 """

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest