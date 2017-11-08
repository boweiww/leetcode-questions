# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
 def addTwoNumbers(self, l1, l2):
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """
  temp=0
  l3s=ListNode(0)
  l3=l3s
  while (l1!= None) or (l2!=None):
   if l1==None:
    a=l2.val+temp
    l2=l2.next
   elif l2==None:
    a=l1.val+temp
    l1=l1.next
   else:
    a=l1.val+l2.val+temp
    l1=l1.next
    l2=l2.next

   if a >=10:
    a=a-10
    temp=1
   else:
    temp=0
   l3.next=ListNode(a)

   l3=l3.next
  if temp==1:
   l3.next=ListNode(1)



  return l3s.next

