class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next
        nodes.sort()

        head = ListNode(0)
        current_node = head
        for i in nodes:
            current_node.next = ListNode(i)
            current_node = current_node.next

        return head.next