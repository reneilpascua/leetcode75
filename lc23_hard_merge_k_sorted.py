# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # unload everything into one list
        s = []
        for l in lists:
            while l:
                s.append(l.val)
                l = l.next
        
        # do one big sort (descending so we can pop from the right end)
        s.sort(reverse=True)

        # create the list from nodes
        l = ListNode()
        c = l
        while s:
            c.next = ListNode(val=s.pop())
            c = c.next
        return l.next