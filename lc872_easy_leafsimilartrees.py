class Solution:
  def leafSimilar(self, root1, root2) -> bool:
    leaves1 = []
    
    s = [root1]
    while s:
      cur = s.pop()
      if cur.left:
        s.append(cur.left)
      if cur.right:
        s.append(cur.right)
      if not (cur.left or cur.right): # is a leaf
        leaves1.append(cur.val)
    
    i = 0
    s = [root2]
    while s: # find leaves and compare w leaves1
      cur = s.pop()
      if cur.left:
        s.append(cur.left)
      if cur.right:
        s.append(cur.right)

      if not (cur.left or cur.right): # is a leaf
        if i >= len(leaves1): # root2 has more leaves than root1
          return False
        
        if cur.val != leaves1[i]:
          return False
        else:
          i += 1
    
    return i == len(leaves1) # false if root1 has more leaves than root2