from collections import defaultdict
from typing import Optional, List
from utils.treenode import TreeNode, create_tree
class Solution:
        
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    # idea
    # use a dict to keep track of pathsums (how often they've appeared)
    pathsum_occurrences = defaultdict(int)

    # dfs will add to pathsum only the sums on the current path.
    # once a dfs call is popped off the stack, we backtrack so that
    # the next path doesn't incorrectly use the previous path's sums.
    def dfs(node, pathsum) -> int:
      nonlocal pathsum_occurrences, targetSum
      if not node: return 0
      
      pathsum += node.val
      
      # explanation:
      # this node is the end of a path that results in targetSum
      # IF the pathsum value (pathsum - targetSum) has appeared in the path.
      # ie. at some past node A, there was a pathsum pA, and at the current node,
      # the pathsum is pA+targetSum. the path after node A until the current
      # node will have pathsum = targetSum.
      count = pathsum_occurrences[pathsum - targetSum]
      # ^ if hasn't seen, then defaultdict inits this val to 0
      
      # add this pathsum to the dict
      pathsum_occurrences[pathsum] += 1

      # how many subpaths after this node satisfy the targetSum condition?
      l = dfs(node.left, pathsum)
      r = dfs(node.right, pathsum)

      # backtrack -- this dfs call is finishing, so the next dfs call in the
      # stack should not have seen this pathsum
      pathsum_occurrences[pathsum] -= 1

      return count + l + r

    pathsum_occurrences[0] = 1
    return dfs(root, 0)


  def pathSum_0(self, root: Optional[TreeNode], targetSum: int) -> int:
    ans = 0

    def dfs_0(node: TreeNode, diffs: List[int]):
      """0th ver. keeps track of many path sums, unnecessary"""
      nonlocal targetSum, ans
      if not node: return
      for d in diffs:
        if node.val == d:
          ans += 1
      new_diffs = [d - node.val for d in diffs] + [targetSum]
      dfs_0(node.left, new_diffs)
      dfs_0(node.right, new_diffs)
    dfs_0(root, [targetSum])
    return ans

if __name__ == '__main__':
  # ex1 = (create_tree([3,5,-3,3,2,None,11,3,-2,None,1]), 8)
  ex2 = (create_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22)
  print(Solution().pathSum(*ex2))