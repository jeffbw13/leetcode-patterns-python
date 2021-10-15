# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        # read list twice
        curr = head
        while curr:
            curr = curr.next
            count = count + 1

        curr = head
        mid = floor(count/2)

        for x in range(1, mid+1):
            curr = curr.next

        return curr