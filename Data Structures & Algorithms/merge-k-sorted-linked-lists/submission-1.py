# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iter(l1, l2):
            if l1.val >= l2.val:
                head = l2
                l2 = l2.next
            else:
                head = l1
                l1 = l1.next
            
            node = head
            while l1 and l2:
                if l1.val >= l2.val:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            
            node.next = l1 or l2
            return head

        if not lists:
            return None

        l1 = lists.pop()
        l2 = lists.pop()
        while len(lists) != 0:
            l1 = iter(l1, l2)
            l2 = lists.pop()

        l1 = iter(l1,l2)
        return l1 