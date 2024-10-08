# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 1:
            raise ValueError(f"Invalid input: k must be a positive integer, got {k}")
            
        head_after_reversing = self.go_forward(head, k-1)

        if k == 1 or not head_after_reversing:
            return head
            
        previous = None
        current = head
        while self.go_forward(current, k-1):
            end = self.reverse_k(previous, current, k)
            previous, current = end, end.next

        return head_after_reversing


    def reverse_k(self, prehead, head, k) -> Optional[ListNode]:
        end = self.go_forward(head, k-1)
        after_end = end.next

        if prehead:
            prehead.next = None

        pre_current = prehead
        current = head
        after_current = head.next
        
        for i in range(k):
            current.next = pre_current
            if i != k-1:
                pre_current, current, after_current = current, after_current, after_current.next

        if prehead:
            prehead.next = end
            
        head.next = after_end
        return head

    def go_forward(self, head, k) -> Optional[ListNode]:
        if not head:
            return None
            
        if k == 0:
            return head
            
        if k < 0:
            raise ValueError("Move forward parameter can't be negative: " + str(k))
            
        count = 0
        current = head
        while current and count <= k-1:
            current = current.next
            count += 1

        return current