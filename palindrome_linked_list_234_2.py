# Version using O(1) space and time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #store values in a list (cheat)
        #palin = []
        curr = head
        last = head
        count = 0

        while curr:
            #palin.append(curr.val)
            count = count+1
            if curr.next:
                curr.next.prev = curr
                last = curr.next
            curr = curr.next

        # we've read to the end, now regress from both ends to middle
        first = head
        mid = floor(count/2)
        count = 1
        while count <= mid:
            if first.val != last.val:
                return False
            first = first.next
            last = last.prev
            count = count + 1

        return True