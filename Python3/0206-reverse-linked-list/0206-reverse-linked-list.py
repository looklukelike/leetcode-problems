# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = None
        while node:
            next_node = node.next
            if next_node:
                print(node.val, next_node.val)
            node.next = prev_node
            prev_node = node
            
            if not next_node:
                break
            else:
                node = next_node

        return node
