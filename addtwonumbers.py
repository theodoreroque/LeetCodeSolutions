"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
return the sum as a linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    numList1 = []
    numList2 = []
    
    
    def linkedListToNumList(self, ll, nl):
        """
        :type ll: ListNode
        :type nl: List[int]
        :rtype: None
        """
        nl.append(ll.val)
        
        while not ll.next == None:
            self.linkedListToNumList(ll.next, nl) 
            return
        return
    
    def numListToInt(self, nl):
        """
        :type nl: List[int]
        :rtype: Int
        """
        strList = [str(x) for x in nl]
        num = "".join(strList)
        return int(num)
            
        
    def numToLinkedList(self, n, nextNode=None):
        """
        :type n: List[str]
        :type nextNode: ListNode
        :rtype: ListNode
        """
        node = n.pop()
        nLN = ListNode(node, nextNode)
        while len(n) > 0:
            nLN = self.numToLinkedList(n, nLN)
        return nLN
        
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Convert Linked List to Number
        nl1 = []
        nl2 = []
        self.linkedListToNumList(l1, nl1)  
        nl1.reverse()
        num1 = self.numListToInt(nl1)
        
        
        self.linkedListToNumList(l2, nl2)
        nl2.reverse()
        num2 = self.numListToInt(nl2)
        
        # Obtain sum
        s = num1 + num2
        
        # Reverse Sum
        sumStr = str(s)
        sumList = [x for x in sumStr]
        sumList.reverse()
        
        
        # Convert reversed sum to Linked List
        nL = self.numToLinkedList(sumList)
        return nL