from typing import Optional
from utils.listnode import ListNode, generate_sorted_linked_list
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
    
    # using a stack
    s = [None]

    cur = head
    while cur:
      s.append(cur)
      cur = cur.next
    
    ans = s[-1]
    cur = s[-1]
    while s:
      cur.next = s.pop()
      cur = cur.next
    
    return ans

if __name__ == '__main__':
  ex1 = generate_sorted_linked_list(5)
  ex2 = generate_sorted_linked_list(10)
  print(Solution().reverseList(ex2))
