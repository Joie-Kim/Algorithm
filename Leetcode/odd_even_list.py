# 328. Odd Even Linked List
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# 72 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        return head