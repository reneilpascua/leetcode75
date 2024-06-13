from typing import Optional
from utils.treenode import TreeNode

class Solution:
  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    
    def dfs(node, pathsum, rightward):
      # rightward = 1 if cur is prev's right; = 0 if cur is prev's left
      if not node: return pathsum-1

      # if go same dir, pathsum reset to 1 (new zigzag)
      l = dfs(node.left, 1 if not rightward else pathsum+1, 0)
      r = dfs(node.right, 1 if rightward else pathsum+1, 1)
      return max(l,r)

    return max(dfs(root.left,1,0), dfs(root.right,1,1))