from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'

def generate_sorted_linked_list(length = 5) -> Optional[ListNode]:
    """
    Generates a linked list of sorted increasing integers
    """
    if length <= 0: return None

    a = ListNode(1)
    cur = a
    l = 1
    while l < length:
        l += 1
        cur.next = ListNode(l)
        cur = cur.next
    return a