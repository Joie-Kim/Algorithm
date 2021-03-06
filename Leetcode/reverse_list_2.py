# 92. Reverse Linked List II
# Reverse a linked list from position m to n. Do it in one-pass.

# 44 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next
        
        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        
        return root.next