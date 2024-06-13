from typing import Optional, List
from collections import deque
from utils.treenode import TreeNode

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    view = []
    q = deque()
    q.append((root,0))
    
    level = -1
    while q:
      cur, clevel = q.popleft()
      if not cur: continue
      
      if clevel > level:
        view.append(cur.val)
        level += 1
      
      q.append((cur.right, clevel+1))
      q.append((cur.left, clevel+1))

    return view