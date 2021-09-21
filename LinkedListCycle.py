# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fastP = slowP = head
        while fastP and slowP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if fastP == slowP:
                return True
            
            
            