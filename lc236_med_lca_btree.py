from typing import List
from utils.treenode import TreeNode, find_node, create_tree

class Solution:
  def lowestCommonAncestor(
    self,
    root: TreeNode, p: TreeNode, q: TreeNode
  ) -> TreeNode:
    if not root: return root # None?

    # root IS the LCA if
    # (A) p and q are in different subtrees of root;
    #   if p and q are in the same subtree, means we can go lower for LCA
    # (B) root is p, and is the ancestor of q (or vice versa)
    
    if root in (p,q): return root

    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r: # ie. p is in one subtree, q in the other. this is lca.
      return root 
    
    # (l or r) = the first non-falsy value, else the first falsy val.
    return l or r

  def lowestCommonAncestor_0(
    self,
    root: TreeNode, p: TreeNode, q: TreeNode
  ) -> TreeNode:
    
    descendants: List[List[TreeNode]] = [] # [0] is descendants of p, [1] is of q
    def dfs(node: TreeNode, descs: List[TreeNode]): # recursive
      nonlocal p, q, descendants
      
      new_descs = descs + [node] # can be your own desc
      if node.val in [p.val, q.val]:
        descendants.append(new_descs)
      if node.left:
        dfs(node.left, new_descs)
      if node.right:
        dfs(node.right, new_descs)
    
    dfs(root, [])
    # print(descendants[0])
    lowest = root
    for r1, r2 in zip(*descendants):
      if r1 == r2:
        lowest = r1

    return lowest

if __name__ == '__main__':
  root1 = create_tree([3,5,1,6,2,0,8,None,None,7,4])
  ex1 = (root1, find_node(root1, 5), find_node(root1, 1))
  ex2 = (root1, find_node(root1, 5), find_node(root1, 4))
  print(Solution().lowestCommonAncestor(*ex2))
