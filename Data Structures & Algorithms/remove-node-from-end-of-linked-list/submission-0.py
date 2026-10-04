# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1, 2, 3, 4] n = 2
        # we want to get node with value 2, then point it its next to next.next
        # slow, fast = 0, 0 (dummy node)
        # n = 0, fast = 1
        # n = 0, fast = 2
        # slow, fast = 0, 2
        # slow, fast = 1, 3
        # slow, fast = 2, 4 (stop here) 

        # [5], n = 1
        # slow, fast = 0, 0
        # n = 0, fast = 5
        # slow, fast = 0, 5 (stop here)

        # slow.next = fast.next.next if fast else None

        # return dummy.head

        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None

        return dummy.next