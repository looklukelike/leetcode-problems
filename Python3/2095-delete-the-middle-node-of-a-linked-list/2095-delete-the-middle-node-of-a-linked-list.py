# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        counter = 0
        node = head
        while node:
            counter += 1
            node = node.next
        middle_node_index = counter // 2

        node = head
        counter = 0
        prev_node = node
        while counter < middle_node_index:
            prev_node = node
            node = node.next
            counter += 1
        prev_node.next = node.next

        return head