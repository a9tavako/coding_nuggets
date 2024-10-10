# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def move_forward(head:Optional[ListNode], k:int) -> Optional[ListNode]:
    if not head:
        return None

    if k == 0:
        return head

    if k < 0:
        raise ValueError(f"Invalid input: {k}")

    current = head
    count = 1
    while current and count <= k:
        current = current.next  
        count += 1

    return current

def get_length(head: Optional[ListNode]) -> int:
    if not head:
        return 0

    current = head
    count = 0
    while current:
        current = current.next
        count += 1

    return count

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        if k == 0:
            return head

        n = get_length(head)
        k = k % n

        if k == 0:
            return head

        new_end = move_forward(head, n-k-1)
        new_head = new_end.next
        end = move_forward(new_end, k)

        new_end.next = None
        end.next = head

        return new_head