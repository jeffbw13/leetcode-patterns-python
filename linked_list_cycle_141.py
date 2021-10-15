# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# WHAT BUILDS THIS LIST?

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # did we catch up?
            if fast == slow:
                return True

        return False