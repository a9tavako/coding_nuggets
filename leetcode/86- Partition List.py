from typing import List

def split_list_by_value(head:ListNode, value: int) -> ListNode:
    if not head:
        return None
        
    less_pre_head = ListNode()
    more_pre_head = ListNode()

    current = head
    current_less = less_pre_head
    current_more = more_pre_head
    while current:
        if current.val < value:
            current_less.next = current
            temp = current
            current = current.next
            temp.next = None
            current_less = current_less.next
            continue

        current_more.next = current
        temp = current
        current = current.next
        temp.next = None
        current_more = current_more.next

    current_less.next = more_pre_head.next

    return less_pre_head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        return split_list_by_value(head, x)