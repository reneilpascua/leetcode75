from typing import Optional
from utils.treenode import TreeNode

class Solution:

  def helper(self, root: TreeNode) -> Optional[TreeNode]:
    """
    replaces the root with root-left and attaches root-right to root-left's
    right-most branch.
    """
    if not root.left: return root.right

    cur = root.left
    while cur and cur.right:
      cur = cur.right
    cur.right = root.right
    return root.left
  
  def deleteNode_iterative(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # edge case: the root is to be deleted
    if root:
      if root.val == key:
        return self.helper(root)
    else:
      return None
    
    # here, key should be found below root.

    # 1. find key, keep prev reference
    # 2. replace it (keeping bst property)
    cur = root
    prev = cur
    direction = -1 # 0 if left, 1 if right
    while cur:
      cval = cur.val
      if key == cval: # stop here
        cur = self.helper(cur)
        if direction: # right
          prev.right = cur
        else: # left
          prev.left = cur
        break
      else: # move on
        prev = cur
        if key < cval:
          cur = cur.left
          direction = 0
        if key > cval:
          cur = cur.right
          direction = 1
    
    return root
  
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # recursive
    if not root: return root

    if key < root.val:
      root.left = self.deleteNode(root.left, key)
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)
    else: # root is to be deleted
      if not root.left: return root.right
      if not root.right: return root.left

      # there's a left and right.
      # replace with root-left; go to the very right of root-left, and
      # that is where you put root-right
      ans = root.left # save a ref to it
      cur = root.left
      while cur and cur.right:
        cur = cur.right
      else: # cur exists but cur.right does not.
        cur.right = root.right
      return ans
    return root

  
  