# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head

        while b:
            c = b.next # save
            b.next = a # flip

            #advance (reset)
            a = b
            b = c

        return a # as this would be new head in the end and b would be None


