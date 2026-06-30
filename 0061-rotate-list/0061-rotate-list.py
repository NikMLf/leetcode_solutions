# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head is None:
            return None
        current_node = head
        nodes = []
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next
        k = k % len(nodes)
        nodes = [i.val for i in nodes]
        left = nodes[len(nodes) - k:].copy()
        nodes = left + nodes[:len(nodes) - k]

        res = ListNode(0)
        current_res_node = res
        for i in nodes:
            current_res_node.next = ListNode(i)
            current_res_node = current_res_node.next
        
        return res.next
        