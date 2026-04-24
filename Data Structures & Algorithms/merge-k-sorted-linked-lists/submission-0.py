# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def rec(l1, l2):
            if not l1:
                return l2
            if not l2: 
                return l1

            if l1.val >= l2.val:
                l2.next = rec(l1, l2.next)
                return l2
            else:
                l1.next = rec(l1.next, l2)
                return l1
            
            return None

        if not lists:
            return None

        l1 = lists.pop()
        l2 = lists.pop()
        while len(lists) >= 1:
            l1 = rec(l1, l2)
            l2 = lists.pop()

        l1 = rec(l1,l2)
        return l1 