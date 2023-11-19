from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while list1 is not None:
            nodes.append(list1)
            list1 = list1.next

        while list2 is not None:
            nodes.append(list2)
            list2 = list2.next

        nodes.sort(key=lambda x: x.val)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0] if len(nodes) > 0 else None
