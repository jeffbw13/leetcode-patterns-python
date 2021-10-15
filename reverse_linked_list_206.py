# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create new list turning pointers around and tail becoming head

        new_list = node = None
        curr = head

        while curr:

            node = ListNode(curr.val)
            node.next = new_list
            new_list = node
            curr = curr.next

        return node