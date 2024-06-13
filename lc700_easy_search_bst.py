from typing import Optional
from utils.treenode import TreeNode

class Solution:
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    cur = root
    while cur:
      cval = cur.val
      if val == cval:
        return cur
      elif val < cval:
        cur = cur.left
      else: # val > cval
        cur = cur.right
    
    return None