# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(prev, head, n):
            if head is None:
                return 1
        
            count = rec(head, head.next, n)

            if count is n:
                if prev is None:
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    prev.next = head.next

            return count + 1

        if not head:
            return None

        if head.next is None and n==1:
            return None

        rec(None, head, n)
        return head