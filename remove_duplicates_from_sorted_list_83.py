# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        while curr:
            #print(curr)
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:    # important! don't advance if changed the pointer
                     # need to consider next turn
                curr = curr.next

        return head