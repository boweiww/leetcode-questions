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
        a=0
        b=0
        list=[]
        if l1 == None: 
            return l2
        elif l2 == None:
            return l1

        while True:
            if l1.val > l2.val:
                list.append(l2.val)
            
                if l2.next == None:
                    
                    while True:
                        list.append(l1.val)
                        if l1.next == None:
                            return list
                        l1=l1.next
                l2=l2.next
            else:
                list.append(l1.val)
                if l1.next == None:
                    while True:
                        list.append(l2.val)
                        if l2.next == None:
                            return list
                        l2=l2.next
                l1=l1.next