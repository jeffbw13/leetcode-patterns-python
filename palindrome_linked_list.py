# This is version 1.
# Version 2 uses O(1) space and time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #store values in a list (cheat)
        palin = []
        curr = head

        while curr:
            palin.append(curr.val)
            curr = curr.next

        start = 0
        end = len(palin) - 1
        while start <= end:
            if palin[start] != palin[end]:
                return False
            start = start+1
            end = end-1

        return True
