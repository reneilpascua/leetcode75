from typing import Optional
from utils.listnode import ListNode

class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    if not head: return 0

    # assume a non-zero amount of pairs, and no singles
    # slow-fast ptr algo for even length list will end when slow is at
    # index len//2
    s = []
    prev = None
    slow, fast = head, head
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
      s.append(prev.val)
    
    # turns out this while loop ends when prev and slow become a pair
    maxsum = prev.val + slow.val # just to init
    cur = prev.next
    while s and cur:
      maxsum = max(
        maxsum,
        s.pop() + cur.val
      )
      cur = cur.next
    
    return maxsum

