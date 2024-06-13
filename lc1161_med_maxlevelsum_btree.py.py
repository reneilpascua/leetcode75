from typing import Optional, List
from collections import deque
from utils.treenode import TreeNode

class Solution:
  def maxLevelSum_0(self, root: Optional[TreeNode]) -> int:
    maxlevelsum = float('-inf')
    maxlevel = 0
    q = deque()
    q.append((root,1))

    level = 1
    levelsum = 0
    N = 1 # the max number of nodes at this level
    n = 0
    while q:
      n += 1
      curnode, curlevel = q.popleft()
    
    return maxlevel
  
  def maxLevelSum_0(self, root: Optional[TreeNode]) -> int:
    # assume root does exist (description says)

    q = deque()
    q.append((root.left, 2))
    q.append((root.right, 2))

    level = maxlevel = 1
    levelsum = maxlevelsum = root.val
    while q:
      curnode, curlevel = q.popleft()
      
      if curlevel > level: # we've finished a level. process the level sum.
        if levelsum > maxlevelsum: # strictly greater!
          maxlevelsum = levelsum
          maxlevel = level
        levelsum = 0
        level += 1
      
      if not curnode: continue
      
      levelsum += curnode.val
      if curnode.left: q.append((curnode.left, level+1))
      if curnode.right: q.append((curnode.right, level+1))
    
    # last level isn't compared to max, so compare it before returning
    return level if levelsum > maxlevelsum else maxlevel