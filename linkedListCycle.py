"""
File: linkedListCycle.py
Author: Me
Email: abdoulayegnbalde@email.com
Github: https://github.com/abdoulayegk
Description: Given head, the head of a linked list, determine if the linked
list has a cycle in it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        while slow and fast and slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
