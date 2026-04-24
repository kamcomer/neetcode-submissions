# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next

        if len(stack) == 0:
            return None

        res = ListNode(stack.pop())
        node = res
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        
        return res
        
        