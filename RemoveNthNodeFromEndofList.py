# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tempNode = ListNode(0,head)
        leftPointer = tempNode
        rightPointer = head
        while n > 0:
            rightPointer = rightPointer.next
            n -= 1
        while rightPointer:
            rightPointer = rightPointer.next
            leftPointer = leftPointer.next

        leftPointer.next = leftPointer.next.next

        return tempNode.next

