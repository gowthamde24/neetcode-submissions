# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head and head.next:
            return None

        slow = head
        fast = head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half = slow.next
        slow.next = None

        curr=second_half
        prev=None

        while curr:
            tmp_val = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_val
        second_half = prev
        first_half = head

        while second_half:
            tmp1 = first_half.next
            tmp2 = second_half.next

            first_half.next = second_half
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2
        
        