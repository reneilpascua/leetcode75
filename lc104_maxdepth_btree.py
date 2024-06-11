from typing import Optional
from utils.treenode import TreeNode

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    
    maxd = 0
    s = [(root, 1)]
    while s:
      cur, d = s.pop()
      maxd = max(maxd, d)
      if cur.left: s.append((cur.left, d+1))
      if cur.right: s.append((cur.right, d+1))
    
    return maxd
