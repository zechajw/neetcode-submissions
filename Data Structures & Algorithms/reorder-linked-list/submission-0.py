# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def splitList(head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
            # so we check for fast and fast.next
            dummy = ListNode(0, head)
            slow, fast = dummy, dummy

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second_head = slow.next
            slow.next = None
            return (dummy.next, second_head)

        # reverse
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        # merge
        def mergeLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0)

            curr = dummy
            curr_list1 = list1
            curr_list2 = list2

            # list2 is guaranteed to be less or equal length to list 1 for this problem
            while curr_list2:
                curr.next = curr_list1
                curr = curr.next
                curr_list1 = curr_list1.next
                curr.next = curr_list2
                curr = curr.next
                curr_list2 = curr_list2.next

            if curr_list1:
                curr.next = curr_list1

            return dummy.next

        list1, list2 = splitList(head)
        list2 = reverseList(list2)
        merged_lists = mergeLists(list1, list2)

