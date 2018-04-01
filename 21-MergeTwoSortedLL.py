# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = ListNode(-1)
        dummy = prev
        while(l1 or l2):
            if(l1 == None):
                prev.next = l2
                prev = prev.next
                l2 = l2.next
            elif(l2 == None):
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                print "here"
                if(l1.val < l2.val):
                    prev.next = l1
                    prev = prev.next
                    l1 = l1.next
                else:
                    prev.next = l2
                    prev = prev.next
                    l2 = l2.next
                
        return dummy.next
