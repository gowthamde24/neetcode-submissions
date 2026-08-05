# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l1
        carry=0

        while l1:
            val1=l1.val
            val2=l2.val if l2 else 0
            total=val1 + val2 + carry

            carry = total // 10
            l1.val=total % 10

            if not l1.next:
                if l2 and l2.next:
                    l1.next=l2.next
                    l2.next=None

                elif carry>0:
                    l1.next=ListNode(carry)
                    carry=0

            l1=l1.next
            l2=l2.next if l2 else None
        return head