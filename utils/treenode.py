from typing import List, Any
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return f'{self.val}'

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
    
if __name__ == '__main__':
  # test tree creation and printing
  vals = [3,9,20,None,None,15,7]
  tree = create_tree(vals)
  # print(tree)
  # print(tree.left)
  # print(tree.right)
  # print(tree.left.left)
  # print(tree.left.right)