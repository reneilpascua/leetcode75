from typing import List
class Solution:
  def findDifference(
    self, 
    nums1: List[int], 
    nums2: List[int]
  ) -> List[List[int]]:
    d1 = set(nums1)
    d2 = set(nums2)
    return [
      [
        dd1 for dd1 in d1 if dd1 not in d2
      ],
      [
        dd2 for dd2 in d2 if dd2 not in d1
      ]
    ]
