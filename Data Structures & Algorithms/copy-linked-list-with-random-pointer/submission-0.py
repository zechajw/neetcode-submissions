"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # for each node, copy it and append it behind the current node
        # keep random as the random pointer to the original node before copy for now
        curr = head

        while curr:
            copy = Node(curr.val, curr.next, curr.random)
            curr.next = copy
            curr = copy.next

        # 1, 2
        # copy = 1'
        # 1 -> 1' -> 2
        # curr = copy.next = 2

        curr = head
        while curr:
            copied_node = curr.next
            copied_node.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # do a second pass to repoint the random of each copied node to random.next 

        # split the second list from the first list
        curr = head
        copied_head = head.next
        copy = head.next

        while copy.next:
            curr.next = curr.next.next
            copy.next = copy.next.next
            curr = curr.next
            copy = copy.next
        
        curr.next = None
        
        return copied_head
