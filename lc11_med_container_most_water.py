from typing import List
class Solution:
  
  def maxArea(self, height: List[int]) -> int:
    # improves on maxArea_0 by skipping iterations of the while loop
    # unless the next height is bigger

    def get_area(x1, h1, x2, h2):
      return (x2-x1)*min(h1,h2)
    
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
      hl, hr = height[l], height[r]
      max_area = max(max_area, get_area(l, hl, r, hr))
      if hl <= hr:
        while l < r and height[l] <= hl:
          l += 1
      else:
        while l < r and height[r] <= hr:
          r -= 1

    return max_area
  
  
  def maxArea_0(self, height: List[int]) -> int:
    
    def get_area(x1, h1, x2, h2):
      return (x2-x1)*min(h1,h2)
    
    l = 0
    r = len(height) - 1
    max_area = 0

    while l < r:
      max_area = max(
        max_area,
        get_area(l, height[l], r, height[r])
      )
      if height[l] <= height[r]:
        l += 1
      else:
        r -= 1

    return max_area