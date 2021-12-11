# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLengthOfList(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    
    def removeNthNode(self, head, n):
        # If the target is the first node
        if n == 0:
            return True
        
        # If the target is not the first node
        index = 1
        while index <= n:
            if index != n:
                head = head.next
            else:
                head.next = head.next.next
            index += 1
        return False
        
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Save the head
        ans = head

        # Get total length of the linked list
        length = self.getLengthOfList(head)

        # Find the index just before the target
        index_before_target = length - n

        # Remove the target
        ## if the target is the head of the list, return True, else False
        removed_first_node = self.removeNthNode(head, index_before_target)
        
        # If the target is the first node
        if removed_first_node:
            return ans.next
        # If the target is not the first node
        else:
            return ans
        