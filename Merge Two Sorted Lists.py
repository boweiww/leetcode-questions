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
                
                
                
# solution of leetcode:
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
# solution from other leetcode users:

    # iteratively
    # Assume ListNode is okay to call (that is not built in on my computer)
    # This is an interesting algorithm
    # keep resetting current node
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
    # recursively    this way is similar to official way
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
    # in-place, iteratively        
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next