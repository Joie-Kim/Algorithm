# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = temp = ListNode()
        
        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            sum_val = l1_val + l2_val + carry
            
            temp.next = ListNode(sum_val % 10)
            temp = temp.next
            
            carry = sum_val // 10
        
        return result.next