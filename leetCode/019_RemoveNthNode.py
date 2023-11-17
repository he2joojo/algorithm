from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        remove_idx = len(nodes) - n
        nodes.append(None)

        if remove_idx == 0:
            return nodes[1]

        nodes[remove_idx - 1].next = nodes[remove_idx + 1]
        return nodes[0]
