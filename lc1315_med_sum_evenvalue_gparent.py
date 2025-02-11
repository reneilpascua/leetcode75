from typing import Optional
from utils.treenode import TreeNode

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sums = 0

        def dfs(node, parent_val):
            nonlocal sums
            if not node: return

            if parent_val%2 == 0:
                sums += node.left.val if node.left else 0
                sums += node.right.val if node.right else 0
            
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return sums

if __name__ == '__main__':
    pass