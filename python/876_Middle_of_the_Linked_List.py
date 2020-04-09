# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def middleNode(self, head: ListNode) -> ListNode:
    #     # count: Length of the linked list
    #     temp = head
    #     count = 0
    #     while (temp):
    #         count += 1
    #         temp = temp.next
        
    #     middle_index = math.ceil((count - 1) / 2)
    #     for _ in range(middle_index):
    #         head = head.next
            
    #     return head

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow