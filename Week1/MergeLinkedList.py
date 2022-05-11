# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:

        vacant = ListNode()
        curr = vacant
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                curr.val = list2.val
                list2 = list2.next
            else:
                curr.val = list1.val
                list1 = list1.next
            curr = curr.next
        if list1 == None:
            curr.next = list2
        elif list2 == None:
            curr.next = list1
        return vacant.next





