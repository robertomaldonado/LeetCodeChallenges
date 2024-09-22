# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next # Temp hold
            curr.next = prev #Reverse ref
            prev = curr #Advance
            curr = next_node #Go to next based on temp hold
        return prev
        