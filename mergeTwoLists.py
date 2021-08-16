# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def compare(a, b):
        if a is None:
            return b
        elif b is None:
            return a
        
        if a.val < b.val:
            return a
        return b
    
    
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode()
        answer = sortedList

        while l1 != None or l2 != None:
            nextNode = ListNode.compare(l1, l2)
            newNode = ListNode(nextNode.val)
            sortedList.next = newNode
            sortedList = sortedList.next
            if nextNode == l1:
                l1 = l1.next
            else:
                l2 = l2.next
            
            if nextNode != None:
                print(nextNode.val)
        
        answer = answer.next
        return answer