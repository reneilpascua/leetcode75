from typing import List, Any, Optional
from collections import deque

class TreeNode:
  def __init__(self, val=0, left:'TreeNode'=None, right:'TreeNode'=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self) -> str:
    # return f'{self.val}, L: ({self.left}), R: ({self.right})'
    return str(self.val)
  
  def __repr__(self) -> str:
    return self.__str__()

def create_tree(vals: List[Any]) -> TreeNode:  
  if not vals: return None
  
  root = TreeNode(val=vals[0])
  parents = deque([root])
  
  cur = parents.popleft()
  counter = 0
  for v in vals[1:]:

    if v:
      t = TreeNode(val=v)
      parents.append(t)
    else:
      t = None

    if counter == 0:
      cur.left = t
      counter += 1
    elif counter == 1:
      cur.right = t
      cur = parents.popleft()
      counter = 0

  return root

def find_node(root, val) -> Optional[TreeNode]:
  """Finds the shallowest TreeNode descendant of root with matching val"""
  if not root: return None

  q: deque[TreeNode] = deque([root])
  while q:
    cur = q.popleft()
    if cur.val == val: return cur
    if cur.left: q.append(cur.left)
    if cur.right: q.append(cur.right)

  return None
    
if __name__ == '__main__':
  # test tree creation and printing
  vals = [3,9,20,None,None,15,7]
  tree = create_tree(vals)
  # print(tree)
  # print(tree.left)
  # print(tree.right)
  # print(tree.left.left)
  # print(tree.left.right)