# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 or not lists:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge2lists(l1,l2))
            lists = mergedLists
        return lists[0]

    def merege2lists(self,l1,l2):
        mergedHead = ListNode()
        dummy = mergedHead

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy = l2.next
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
        return mergedHead
