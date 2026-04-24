# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get LL len
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        

        # Seperate LLs
        count = length / 2
        l1 = head
        l2 = head
        prev = None
        while count > 0:
            prev = l2
            l2 = l2.next
            count -= 1
        
        prev.next = None

        # Reverse LL
        tmp = None
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
        l2 = prev
        
        ptr = head
        flag = True
        l1 = l1.next
        while l1 and l2:
            if flag:
                ptr.next = l2
                l2 = l2.next
            else:
                ptr.next = l1
                l1 = l1.next

            ptr = ptr.next
            flag = not flag
        ptr.next = l1 or l2
        





