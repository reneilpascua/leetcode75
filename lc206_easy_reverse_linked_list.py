from utils.listnode import ListNode, generate_sorted_linked_list
from typing import Optional

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        prev = None
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        cur.next = prev
        return cur

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        t = head.next
        head.next = None
        first = self.reverseListRecursive(t)
        self._joinLists(first, head)
        return first

    def reverseListRecursive_half(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        fast = head
        pre = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        # at this point, slow should be halfway through the list
        t = slow
        pre.next = None

        joined = self._joinLists(
            self.reverseListRecursive_half(t),
            self.reverseListRecursive_half(head)
        )
        # print('joined:', joined)
        return joined

    
    def _joinLists(self, l1, l2) -> Optional[ListNode]:
        if not l1: return l2
        
        # find the end of l1
        c = l1
        while c.next:
            c = c.next
        c.next = l2
        
        return l1
        
if __name__ == '__main__':
    from utils.performance import timer

    @timer
    def time_iterative(testcase):
        return Solution().reverseListIterative(testcase)

    @timer
    def time_recursive(testcase):
        # return Solution().reverseListRecursive_half(testcase)
        return Solution().reverseListRecursive(testcase)

    N = 100
    iterative = time_iterative(generate_sorted_linked_list(N))
    recursive = time_recursive(generate_sorted_linked_list(N))

    print('iterative run (sec): ', iterative[1])
    print('recursive run (sec): ', recursive[1])