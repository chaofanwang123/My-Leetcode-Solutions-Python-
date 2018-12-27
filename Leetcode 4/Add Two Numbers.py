# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=0
        num1=0
        while l1!=None:
            digit=l1.val
            num1=num1+digit*pow(10,i)
            l1=l1.next
            i+=1
        num2=0
        i=0
        while l2!=None:
            digit=l2.val
            num2=num2+digit*pow(10,i)
            l2=l2.next
            i+=1
        num=num1+num2
        m=0
        while pow(10,m)<=num:      
            m+=1
        if m==0:
            return [0]
        l3=[0]*m
        for j in range(m):
            l3[j]=num//pow(10,j)%10
        return l3

