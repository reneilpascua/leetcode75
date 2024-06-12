from utils.treenode import TreeNode
class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    ans = 0
    
    def dfs(node, curmax):
      nonlocal ans
      
      if not node: return
      if node.val >= curmax:
        curmax = node.val
        ans += 1
      
      dfs(node.left, curmax)
      dfs(node.right, curmax)

    dfs(root, root.val)
    return ans