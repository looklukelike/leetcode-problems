# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        node = head
        node_vals = dict()

        n = 0
        while node:
            node = node.next
            n += 1

        i = 0
        node = head
        while node:
            node_vals[i] = node.val
            twin_idx = n - 1 - i
            if twin_idx in node_vals:
                sm = node.val + node_vals[twin_idx]
                max_sum = max(max_sum, sm)
            node = node.next
            i += 1

        return max_sum