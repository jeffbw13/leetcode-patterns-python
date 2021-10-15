# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = l1
        list2 = l2
        new_list = None
        new_head = None
        while list1 or list2:
            if list1 and (list2 == None or list1.val <= list2.val):
                if new_list:
                    new_list.next = list1
                new_list = list1
                list1 = list1.next
            else:
                if list2:
                    if new_list:
                        new_list.next = list2
                    new_list = list2
                    list2 = list2.next
            if new_head == None:
                new_head = new_list

        return new_head