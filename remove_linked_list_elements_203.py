# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        curr = head
        new_list = new_head = None

        while curr:
            if curr.val != val:
                node = ListNode(curr.val)
                if new_list != None:
                    new_list.next = node
                    new_list = node
                else:
                    new_list = node
                    new_head = new_list

            curr = curr.next

        return new_head