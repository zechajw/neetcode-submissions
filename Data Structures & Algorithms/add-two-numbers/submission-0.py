# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        # dummy node
        summed_list = ListNode(0, None)
        
        curr = summed_list

        while l1 or l2:
            digit_addition = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            if digit_addition >= 10:
                carry = 1
            else:
                carry = 0

            next_node = ListNode(digit_addition % 10, None)
            curr.next = next_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            curr.next = ListNode(carry, None)

        return summed_list.next